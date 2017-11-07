# 简单工厂模式
# 简单工厂无需实例化工厂
class Burger():
    name = ""
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class CheeseBurger(Burger):
    def __init__(self):
        self.name = "cheese burger"
        self.price = 10.0


class SpicyChickenBurger(Burger):
    def __init__(self):
        self.name = "spicy chicken burger"
        self.price = 15.0


class Snack():
    name = ""
    price = 0.0
    type = "SNACK"

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class Chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class ChickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0


class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class Coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class Milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0


class FoodFactory():
    @classmethod
    def createFood(cls, FoodClass):
        print(cls.type, " factory produce a instance")
        foodInstance = FoodClass()
        return foodInstance


class BurgerFactory(FoodFactory):
    type = "BURGER"


class SnackFactory(FoodFactory):
    type = "SNACK"


class BeverageFactory(FoodFactory):
    type = "BEVERAGE"


if __name__ == '__main__':
    cheese_burger = BurgerFactory.createFood(CheeseBurger)
    print(cheese_burger.getName(),cheese_burger.getPrice())
    chicken_wings = SnackFactory.createFood(ChickenWings)
    print(chicken_wings.getName(),chicken_wings.getPrice())
    coke = BeverageFactory.createFood(Coke)
    print(coke.getName(),coke.getPrice())