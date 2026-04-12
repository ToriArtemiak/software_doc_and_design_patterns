from database import SessionLocal
from models.models import Product, Category
from data_access.interfaces import IProductRepository, ICategoryRepository


class ProductRepository(IProductRepository):

    def add_product(self, product):
        session = SessionLocal()
        session.add(product)
        session.commit()
        session.close()

    def get_products(self):
        session = SessionLocal()
        products = session.query(Product).all()
        session.close()
        return products


class CategoryRepository(ICategoryRepository):

    def add_category(self, category):
        session = SessionLocal()
        session.add(category)
        session.commit()
        session.close()

    def get_categories(self):
        session = SessionLocal()
        categories = session.query(Category).all()
        session.close()
        return categories