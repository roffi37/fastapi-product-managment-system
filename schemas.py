from datetime import datetime

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: float

    class Config:
        from_attributes = True


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    created_at: datetime
