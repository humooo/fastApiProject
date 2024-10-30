from sqlalchemy.orm import Session
import models
import schemas


def get_category(db: Session, category_id: int):
    return db.query(models.ProductCategory).filter(models.ProductCategory.id == category_id).first()


def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ProductCategory).offset(skip).limit(limit).all()


def create_category(db: Session, category: schemas.ProductCategoryCreate):
    db_category = models.ProductCategory(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        category_id=product.category_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
