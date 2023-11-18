import csv
from FoodProduct import FoodProduct, Unit

class RecipeHandler:
    def __init__(self, csv_file):
        self.products = self.load_products(csv_file)

    def load_products(self, csv_file):
        products = {}
        with open(csv_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                product = FoodProduct(
                    product_id=row['id'],
                    food_type=row['foodName'],
                    product_name=row['productName'],
                    price=float(row['price'][1:]),
                    quantity=float(row['quantity']),
                    unit=Unit(row['unit'])
                )
                products[product.foodType] = product
        return products

    def check_ingredient_availability(self, ingredient_list):
        for ingredient in ingredient_list:
            product = self.products.get(ingredient['name'])
            if product:
                required_quantity = ingredient['quantity']
                if product.quantity >= required_quantity:
                    print(f"{ingredient['name']} is available in sufficient quantity.")
                else:
                    print(f"{ingredient['name']} is not available in sufficient quantity.")
            else:
                print(f"{ingredient['name']} is not found.")

'''Example use:
recipe_handler = RecipeHandler('src/Grocery Items Dataset - Sheet1.csv')
ingredients = [
    {'name': 'Eggs', 'quantity': 200, 'unit': Unit.G},
    {'name': 'Whole Milk', 'quantity': 500, 'unit': Unit.ML}
]
recipe_handler.check_ingredient_availability(ingredients)
'''