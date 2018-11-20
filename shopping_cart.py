class ShoppingCart(object):
    items_in_cart = {}

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        if product not in self.items_in_cart:
            self.items_in_cart[product] = price
            print("%s was added." % product)
        else:
            print("%s is already in the cart" % product)

    def remove_item(self, product):
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print("%s was removed" % product)
        else:
            print("%s is not in the cart" % product)


cris_cart = ShoppingCart("Cris")
cris_cart.add_item("Refrigerator", 125)
cris_cart.add_item("Brocoli", 2)
cris_cart.add_item("GameStation", 10)
cris_cart.add_item("Brocoli", 150)
cris_cart.remove_item("GameStation")
cris_cart.remove_item("A Car")
print(cris_cart.items_in_cart)
