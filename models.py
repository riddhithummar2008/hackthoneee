from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum

class RoleEnum(str, enum.Enum):
    admin = "admin"
    manager = "manager"
    employee = "employee"

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    country = Column(String)
    currency = Column(String)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(Enum(RoleEnum))
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company")

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String)
    description = Column(String)
    amount = Column(Float)
    currency = Column(String)
    company_currency_amount = Column(Float)
    status = Column(String, default="pending")
    date = Column(Date)
class CurrencyRate(Base):
     __tablename__ = "currency_rates"
     id = Column(Integer, primary_key=True)
     country = Column(String)
     currency = Column(String)
     rate_to_usd = Column(Float)

