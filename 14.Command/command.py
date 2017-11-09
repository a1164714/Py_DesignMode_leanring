# 命令模式定义：将一个请求封装为一个对象，从而可以使用不同的请求将客户端参数化，对请求排队或者记录请求日志，可以提供命令的撤销和恢复功能。
# 命令模式中通常涉及三类对象的抽象：Receiver（BackSys），Command，Invoker（WaiterSys）。
#   只有一个Invoker的命令模式也可以抽象成一个类似的“星形网络”，
#   但与之前介绍的中介者模式不同，单纯的命令模式更像是一个辐射状的结构，
#   由Invoker直接对Receiver传递命令，而一般不反向传递，
#   中介者模式“星形网络”的中心，是个协调者，抽象结节间的信息流全部或者部分是双向的。
#   另外，命令模式的定义中提到了“撤销和恢复功能”，
#   也给了各位开发人员一个命令模式使用过程中的建议：各个Receiver中可以设计一个回滚接口，支持命令的“撤销”
#
# 优点：
#       1、低耦合：调用者和接收者之间没有什么直接关系，二者通过命令中的execute接口联系；
#       2、拓展性好：新命令很容易加入，也很容易拼出“组合命令”。
#
# 缺点：
#       1、如果业务场景中命令比较多，那么对应命令类和命令对象的数量也会增加，这样系统会膨胀得很大。
#
# 应用：
#       1、触发-反馈机制的系统，都可以使用命令模式思想。
#           如基于管道结构的命令系统（如SHELL），可以直接套用命令模式；
#           此外，GUI系统中的操作反馈（如点击、键入等），也可以使用命令模式思想。
#
###### 饭店点餐系统 ######
#   这次的点餐系统是个饭店的点餐系统。
#   饭店的点餐系统有什么不同嘛？
#   大伙想想看，在大多数饭店中，当服务员已经接到顾客的点单，录入到系统中后，根据不同的菜品，会有不同的后台反应。
#   比如，饭店有凉菜间、热菜间、主食间，那当服务员将菜品录入到系统中后，凉菜间会打印出顾客所点的凉菜条目，热菜间会打印出顾客所点的热菜条目，主食间会打印出主食条目。
#   那这个系统的后台模式该如何设计？
#   当然，直接在场景代码中加if…else…语句判断是个方法，可这样做又一次加重了系统耦合，违反了单一职责原则，遇到系统需求变动时，又会轻易违反开闭原则。
#   可以将该系统设计成前台服务员系统和后台系统，后台系统进一步细分成 主食子系统，凉菜子系统，热菜子系统。
class BackSys:
    def cook(self, dish):
        pass


class MainFoodSys(BackSys):
    def cook(self, dish):
        print("MainFood:Cook is %s" % dish)


class CoolDishSys(BackSys):
    def cook(self, dish):
        print("COOLDISH:Cook %s" % dish)


class HotDishSys(BackSys):
    def cook(self, dish):
        print("HOTDISH:Cook %s" % dish)


# 前台系统
class WaiterSys():
    menu_map = dict()
    commandList = []

    def setOrder(self, command):
        print("WAITER:Add dish")
        self.commandList.append(command)

    def cancelOrder(self, command):
        print("WAITER:Cancel order...")
        self.commandList.remove(command)

    def notify(self):
        print("WAITER:Nofify...")
        for command in self.commandList:
            command.execute()


class Command():
    receiver = None

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        pass


class FoodCommand(Command):
    dish = ""

    def __init__(self, receiver, dish):
        self.receiver = receiver
        self.dish = dish

    def execute(self):
        self.receiver.cook(self.dish)


class MainFoodCommand(FoodCommand):
    pass


class CoolDishCommand(FoodCommand):
    pass


class HotDishCommand(FoodCommand):
    pass


# 菜单类来辅助业务
class menuAll:
    menu_map = dict()

    # 按种类分类
    def loadMenu(self):  # 加载菜单，这里直接写死
        self.menu_map["hot"] = ["Yu-Shiang Shredded Pork", "Sauteed Tofu, Home Style", "Sauteed Snow Peas"]
        self.menu_map["cool"] = ["Cucumber", "Preserved egg"]
        self.menu_map["main"] = ["Rice", "Pie"]

    def isHot(self, dish):
        if dish in self.menu_map["hot"]:
            return True
        return False

    def isCool(self, dish):
        if dish in self.menu_map["cool"]:
            return True
        return False

    def isMain(self, dish):
        if dish in self.menu_map["main"]:
            return True
        return False


if __name__ == "__main__":
    dish_list = ["Yu-Shiang Shredded Pork", "Sauteed Tofu, Home Style", "Cucumber", "Rice"]  # 顾客点的菜
    waiter_sys = WaiterSys()
    main_food_sys = MainFoodSys()
    cool_dish_sys = CoolDishSys()
    hot_dish_sys = HotDishSys()
    menu = menuAll()
    menu.loadMenu()
    for dish in dish_list:
        if menu.isCool(dish):
            cmd = CoolDishCommand(cool_dish_sys, dish)
        elif menu.isHot(dish):
            cmd = HotDishCommand(hot_dish_sys, dish)
        elif menu.isMain(dish):
            cmd = MainFoodCommand(main_food_sys, dish)
        else:
            continue
        waiter_sys.setOrder(cmd)
    waiter_sys.notify()
