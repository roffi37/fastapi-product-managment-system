from sqlalchemy import (
    Column,
    Integer,
    String,
    DECIMAL,
    DATETIME,
    func
)

from db.engine import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(DECIMAL)
    created_at = Column(DATETIME, default=func.now())
