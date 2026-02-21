from pydantic import BaseModel
from typing import Optional


# ─── User Schemas ────────────────────────────────────────────────

class UserCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None


class UserResponse(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None


# ─── Product Schemas ─────────────────────────────────────────────

class ProductCreate(BaseModel):
    sku: str
    name: str
    price: float
    stock: int
    description: Optional[str] = None


class ProductResponse(BaseModel):
    sku: str
    name: str
    price: float
    stock: int
    description: Optional[str] = None
