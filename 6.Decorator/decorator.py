# 定义：动态地给一个对象添加职责。在增加功能方面，装饰器模式比生成子类更为灵活
#
# AOP 即Aspect Oriented Programming，面向切面编程：如果几个或更多个逻辑过程中（这类逻辑过程可能位于不同的对象，不同的接口当中），有重复的操作行为，就可以将这些行为提取出来（即形成切面），进行统一管理和维护。
#  举例子说，系统中需要在各个地方打印日志，就可以将打印日志这一操作提取出来，作为切面进行统一维护。
#
# 优点：
#       1、装饰器模式是继承方式的一种替代，可以轻量级的拓展被装饰对象的功能
#       2、Python的装饰器模式是实现AOP的一种方式，便于相同操作位于不同调用位置的统一管理
#
# 缺点：
#       1、多层装饰器的调试和维护比较难维护
#
# 应用：
#       1、拓展或增强或减弱一个类的功能。

# 添加日志
class LogManager:
    @staticmethod
    def log(func):
        def wrapper(args, *kw):
            print("visit Func %s" % func.__name__)
            return func(args, *kw)

        return wrapper


######## 快餐点餐系统（饮料加糖加冰系统） ###########
class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"

    @LogManager.log
    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    @LogManager.log
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


class DrinkDecorator():
    def getName(self):
        pass

    def getPrice(self):
        pass


class IceDecorator(DrinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + "(ice)"

    def getPrice(self):
        return self.beverage.getPrice() + 0.3


class SugerDecorator(DrinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + "(suger)"

    def getPrice(self):
        return self.beverage.getPrice() + 0.5


if __name__ == "__main__":
    coke = Coke()
    print("Coke:%s" % coke.getName() + ",price:%s" % coke.getPrice())
    ice_coke = IceDecorator(coke)
    print("Ice_Coke:%s" % ice_coke.getName() + ",price:%s" % ice_coke.getPrice())
