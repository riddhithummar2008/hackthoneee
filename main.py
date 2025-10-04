from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import crud, models, schemas

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Expense Manager (Local SQLite)")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/company")
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    return crud.create_company(db, company.name, company.country, company.currency)

@app.post("/user")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user.name, user.email, user.password, user.role, user.company_id)

@app.post("/expense")
def submit_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, expense.employee_id, expense.category, expense.description,
                               expense.amount, expense.currency, expense.company_currency)

@app.put("/expense/{expense_id}/{status}")
def update_expense(expense_id: int, status: str, db: Session = Depends(get_db)):
    return crud.update_expense_status(db, expense_id, status)

@app.get("/")
def root():
    return {"message": "Expense Manager running locally with SQLite!"}
