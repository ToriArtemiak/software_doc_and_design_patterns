from abc import ABC, abstractmethod

class IProductRepository(ABC):

    @abstractmethod
    def add_product(self, product):
        pass

    @abstractmethod
    def get_products(self):
        pass


class ICategoryRepository(ABC):

    @abstractmethod
    def add_category(self, category):
        pass

    @abstractmethod
    def get_categories(self):
        pass