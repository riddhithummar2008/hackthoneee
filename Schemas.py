from pydantic import BaseModel
from datetime import date

class CompanyCreate(BaseModel):
    name: str
    country: str
    currency: str

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str
    company_id: int

class ExpenseCreate(BaseModel):
    employee_id: int
    category: str
    description: str
    amount: float
    currency: str
    company_currency: str

class ExpenseOut(BaseModel):
    id: int
    category: str
    amount: float
    currency: str
    company_currency_amount: float
    status: str
    date: date

    class Config:
        orm_mode = True
