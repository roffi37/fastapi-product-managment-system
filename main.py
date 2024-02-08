from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from crud import (
    get_products,
    get_product,
    create_product,
    update_product,
    delete_product
)
from db.engine import get_db
from schemas import ProductCreate

app = FastAPI()


@app.get("/products/")
def get_products_main(db=Depends(get_db)):
    return get_products(db)


@app.get("/products/{product_id}/")
def get_product_by_id(product_id: int, db=Depends(get_db)):
    return get_product(db, product_id)


@app.post("/products/")
def create_product_main(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)


@app.put("/products/{product_id}/")
def update_product_by_id(product_id: int, product_update: ProductCreate, db: Session = Depends(get_db)):
    db_product = update_product(db, product_id, product_update)
    return db_product


@app.delete("/products/{product_id}/")
def delete_product_by_id(product_id: int, db: Session = Depends(get_db)):
    db_product = delete_product(db, product_id)
    return db_product
