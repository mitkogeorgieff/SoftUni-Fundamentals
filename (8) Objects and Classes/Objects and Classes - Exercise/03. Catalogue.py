class Catalogue:
    def __init__(self, name_of_prod):
        self.name = name_of_prod
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return [product for product in self.products if product[0].lower() == first_letter.lower()]

    def __repr__(self):
        res_string = f'Items in the {self.name} catalogue:'

        for product in sorted(self.products):
            res_string += '\n' + product

        return res_string


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
