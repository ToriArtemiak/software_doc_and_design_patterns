from database import init_db
from data_access.repositories import ProductRepository, CategoryRepository
from services.product_service import ProductService

init_db()

product_repo = ProductRepository()
category_repo = CategoryRepository()

service = ProductService(product_repo, category_repo)

service.import_from_csv("csv_module/data.csv")

print("Data imported successfully")