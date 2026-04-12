from abc import ABC, abstractmethod

class IProductAPI(ABC):

    @abstractmethod
    def load_products(self):
        pass