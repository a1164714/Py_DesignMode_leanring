#  定义: 将一个复杂的对象的构建与它的表示分离，使得同样构建过程能够创建不同的表示

#  作用: 构建与表示分离，达到解耦的目的。

#  对于建造者模式需要有顺序构建时，可以使用Director

#  应用：
# 1、目标对象由组件构成的场景中，很适合建造者模式。
#   例如，在一款赛车游戏中，车辆生成时，需要根据级别、环境等，选择轮胎、悬挂、骨架等部件，构造一辆“赛车”；
# 2、在具体的场景中，对象内部接口需要根据不同的参数而调用顺序有所不同时，可以使用建造者模式。
#   例如：一个植物养殖器系统，对于某些不同的植物，浇水、施加肥料的顺序要求可能会不同，因而可以在Director中维护一个类似于队列的结构，在实例化时作为参数代入到具体建造者中。

# 优点：
# 1、封装好，用户无需知道对象内部如何构建
# 2、系统拓展简单
# 3、很容易实现“流水线”
# 4、便于细节控制

# 缺点：
# 1、加工工艺对用户不透明

######## 快餐点餐系统（订单系统） ###########
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


class OrderBuilder():
    bBurger = ""
    bSnack = ""
    bBeverage = ""

    def addBurger(self, xBurger):
        self.bBurger = xBurger

    def addSnack(self, xSnack):
        self.bSnack = xSnack

    def addBeverage(self, xBeverage):
        self.bBeverage = xBeverage

    def build(self):
        return Order(self)


class Order():
    buger = ""
    snack = ""
    beverage = ""

    def __init__(self, OrderBuilder):
        self.buger = OrderBuilder.bBurger
        self.snack = OrderBuilder.bSnack
        self.beverage = OrderBuilder.bBeverage

    def show(self):
        print("Burger:%s" % self.buger.getName())
        print("Snack:%s" % self.snack.getName())
        print("Beverage:%s" % self.beverage.getName())


class OrderDirector():
    order_builder = ""

    def __init__(self, order_builder):
        self.order_builder = order_builder

    def createOrder(self, burger, snack, beverage):
        self.order_builder.addBurger(burger)
        self.order_builder.addSnack(snack)
        self.order_builder.addBeverage(beverage)
        return self.order_builder.build()


if __name__ == '__main__':
    order_builder = OrderBuilder()

    ### 第一种
    # order_builder.addBurger(SpicyChickenBurger())
    # order_builder.addSnack(Chips())
    # order_builder.addBeverage(Milk())
    # order_1 = order_builder.build()
    # order_1.show()

    ### 第二种：对于构建有顺序要求时使用
    order_director = OrderDirector(order_builder)
    order_1 = order_director.createOrder(SpicyChickenBurger(), Chips(), Milk())
    order_1.show()
