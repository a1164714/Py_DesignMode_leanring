# 工厂模式
# 优点：
#      封装性好，代码结构清晰
#      屏蔽产品类，业务场景与产品功能细节分开
# 缺点：
#       工厂模式需要实例化工厂，小项目不适合使用
#       产品类拓展比较麻烦，产品拓展同时，抽象工厂也要拓展
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
    type = ""

    def createFood(self, FoodClass):
        print(self.type, " factory produce a instance")
        foodInstance = FoodClass()
        return foodInstance


class BurgerFactory(FoodFactory):
    def __init__(self):
        self.type = "BURGER"


class SnackFactory(FoodFactory):
    def __init__(self):
        self.type = "SNACK"


class BeverageFactory(FoodFactory):
    def __init__(self):
        self.type = "BEVERAGE"


if __name__ == '__main__':
    burger_factory = BurgerFactory()
    snack_factory = SnackFactory()
    beverage_factory = BeverageFactory()
    cheese_burger = burger_factory.createFood(CheeseBurger)
    print(cheese_burger.getName(),cheese_burger.getPrice())
    chicken_wings = snack_factory.createFood(ChickenWings)
    print(chicken_wings.getName(),chicken_wings.getPrice())
    coke = beverage_factory.createFood(Coke)
    print(coke.getName(),coke.getPrice())

