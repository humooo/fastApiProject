from pydantic import BaseModel
from typing import Optional


class ProductCategoryCreate(BaseModel):
    name: str
    description: Optional[str] = None


class ProductCategory(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    category_id: int
    name: str
    description: Optional[str] = None
    price: float


class Product(BaseModel):
    id: int
    category_id: int
    name: str
    description: Optional[str] = None
    price: float

    class Config:
        orm_mode = True
