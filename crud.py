from models import CurrencyRate

def convert_currency_db(db, amount, from_currency, to_currency):
    rates = {r.currency: r.rate_to_usd for r in db.query(CurrencyRate).all()}
    if from_currency not in rates or to_currency not in rates:
        return amount
    rate = rates[to_currency] / rates[from_currency]
    return round(amount * rate, 2)
from sqlalchemy.orm import Session
from models import Company, User, Expense
from datetime import date
import convert_currency from convert_currency


# Create company
def create_company(db: Session, name: str, country: str, currency: str):
    company = Company(name=name, country=country, currency=currency)
    db.add(company)
    db.commit()
    db.refresh(company)
    return company

# Create user
def create_user(db: Session, name: str, email: str, password: str, role: str, company_id: int):
    user = User(name=name, email=email, password=password, role=role, company_id=company_id)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Submit expense
def create_expense(db: Session, employee_id: int, category: str, description: str,
                   amount: float, currency: str, company_currency: str):
    converted = convert_currency(amount, currency, company_currency)
    expense = Expense(employee_id=employee_id, category=category, description=description,
                      amount=amount, currency=currency, company_currency_amount=converted, date=date.today())
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

# Approve/reject expense
def update_expense_status(db: Session, expense_id: int, status: str):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if expense:
        expense.status = status
        db.commit()
        db.refresh(expense)
    return expense
