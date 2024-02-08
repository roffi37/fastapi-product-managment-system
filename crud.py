from sqlalchemy.orm import Session
from models import Product
from schemas import ProductCreate


def create_product(db: Session, product: ProductCreate):
    product_dict = product.model_dump()
    db_product = Product(**product_dict)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session):
    return db.query(Product).all()


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def update_product(db: Session, product_id: int, product_to_update: ProductCreate):
    product_dict = product_to_update.dict(exclude_unset=True)
    db_product = db.query(Product).filter(Product.id == product_id).update(product_dict)
    db.commit()
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product
