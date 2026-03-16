import pandas as pd
from models.models import Product, Category

class ProductService:

    def __init__(self, product_repo, category_repo):
        self.product_repo = product_repo
        self.category_repo = category_repo

    def import_from_csv(self, file_path):

        data = pd.read_csv(file_path)

        categories = {}

        for _, row in data.iterrows():

            category_name = row["category"]

            if category_name not in categories:
                category = Category(name=category_name)
                self.category_repo.add_category(category)
                categories[category_name] = category

            product = Product(
                name=row["name"],
                price=row["price"],
                quantity=row["quantity"],
                category=categories[category_name]
            )

            self.product_repo.add_product(product)