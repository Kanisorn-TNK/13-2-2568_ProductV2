class Product:
    def __init__(self, name, price, stock, brand):
        self.name = name
        self.__price = price
        self.__stock = stock
        self.brand = brand

    def edit(self, val):
        if val == "stock":
            print("Stock Editor")
            val_stock = int(input("Enter stock adjustment: "))
            self.__stock += val_stock
        elif val == "price":
            print("Price Editor")
            val_price = int(input("Enter price adjustment: "))
            self.__price += val_price

    def get_info(self):
        return f"Product - Name: {self.name}, Price: {self.__price}, Stock: {self.__stock}"


class Smartphone(Product):
    def __init__(self, name, price, stock, brand, system):
        super().__init__(name, price, stock, brand)
        self.system = system

    def get_info(self):
        return f"Smartphone - Name: {self.name}, Price: {self._Product__price}, Stock: {self._Product__stock}, Brand: {self.brand}, System: {self.system}"
    
class Laptop(Product):
    def __init__(self, name, price, stock, brand, system):
        super().__init__(name, price, stock, brand)
        self.system = system

    def get_info(self):
        return f"Laptop - Name: {self.name}, Price: {self._Product__price}, Stock: {self._Product__stock}, Brand: {self.brand}, System: {self.system}"
    
class Cloth(Product):
    def __init__(self, name, price, stock, brand, size):
        super().__init__(name, price, stock, brand)
        self.size = size

    def get_info(self):
        return f"Cloth - Name: {self.name}, Price: {self._Product__price}, Stock: {self._Product__stock}, Brand: {self.brand}, System: {self.size}"

smartphone1 = Smartphone("iPhone 15", 45000, 200, "Apple", "IOS")
smartphone1.edit("stock")
smartphone1.edit("price")
print(smartphone1.get_info())

laptop1 = Laptop("Acer NITRO AN515-43-R0T3 Black", 20990, 20, "ACER", "Window")
laptop1.edit("stock")
laptop1.edit("price")
print(laptop1.get_info())

cloth1 = Cloth("Slim-Fit Jeans", 9500, 200, "Versace","29-44")
cloth1.edit("stock")
cloth1.edit("price")
print(cloth1.get_info())