class item:
    all = []
    overide_discount = 0.1  # 10% discount for all items

    # Below type dec in def will work to enforme type validation and for checking other validation we can use assertions
    # def __init__(self, price: float, quantity: float, discount: float):
    # pas
    def __init__(self, price: float, quantity: float, discount: float):
        print(
            f'price is {price}  quantity is {quantity}  discount is {discount}')
        assert price >= 0, "Price must be non-negative"
        assert quantity > 0, "Quantity must be non-negative"
        assert discount >= 0, "Discount must be non-negative"
        assert isinstance(price, (float, int)), "Price must be a number"
        assert isinstance(quantity, (float, int)), "Quantity must be a number"
        assert isinstance(discount, (float, int)), "Discount must be a number"

        # if not isinstance(price, (float, int)) or not isinstance(quantity, (float, int)) or not isinstance(discount, (float, int)):
        #     raise ValueError(
        #         "Constructor called:  Price, quantity, and discount must be number")

        # if price < 0 or quantity < 0 or discount < 0:
        #     raise ValueError(
        #         "Constructor called:  Price, quantity, and discount must be non-negative")

        self.price = price
        self.quantity = quantity
        self.discount = discount
        item.all.append(self)

    def calculate_total_price(self):
        total_price = self.price * self.quantity
        total_discount = total_price * self.discount
        return total_price - total_discount

    def apply_overide_discount(self):
        self.discount = item.overide_discount
        total_price = self.price * self.quantity
        total_discount = total_price * self.discount
        return total_price - total_discount

    def __repr__(self):
        return f"item(price={self.price}, quantity={self.quantity}, discount={self.discount})"


item1 = item(100, 2, 0.2)  # 20% discount
item2 = item(200, 1, 0.15)  # 15% discount
item3 = item(50, 5, 0.05)   # 5% discount
# print(item1.calculate_total_price())  # Output: 160.0
# print(item2.calculate_total_price())  # Output: 170.0
# print(item3.calculate_total_price())  # Output: 237.5
# print(item1.apply_overide_discount())  # Output: 180.0

# print(item.__dict__)
# print(item1.__dict__)
# print(item2.__dict__)
# print(item3.__dict__)
# print(item1)
# print(item.all)

for i in item.all:
    print(f'Items added  {i}')

# del item1
print(item.all)

item4 = item(50, 65, 0.05)
