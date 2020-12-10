from ..repository.price_repository import PriceRepository


class PriceController:
    def __init__(self):
        self.price_repository = PriceRepository()

    def insert_price(self, price):
        self.price_repository.insert(price)

    def get_product_list(self):
        return self.price_repository.get_distinct_price()

    def get_price_information(self, request):
        params = {}
        if request.json['action'] == "L":
            products = self.price_repository.get_distinct_price()
            return products
        else:
            for param in request.json:
                if param == 'action':
                    pass
                else:
                    params[param] = request.json[param]

            prices = self.price_repository.get_one(params)
            return prices