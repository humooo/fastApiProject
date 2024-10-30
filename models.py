from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from database import Base


class ProductCategory(Base):
    __tablename__ = "product_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(DECIMAL, nullable=False)
    category_id = Column(Integer, ForeignKey("product_categories.id"))

    category = relationship("ProductCategory", back_populates="products")
