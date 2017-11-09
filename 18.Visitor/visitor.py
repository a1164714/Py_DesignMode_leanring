# 访问者模式的定义如下：封装一些作用于某种数据结构中的各元素的操作，它可以在不改变数据结构的前提下定义于作用于这些元素的新操作。
#   提到访问者模式，就不得不提一下双分派。
#   分派分为静态分派和动态分派。
#       首先解释下静态分派，静态分派即根据请求者的名称和接收到的参数，决定多态时处理的操作。
#       比如在Java或者C++中，定义名称相同但参数不同的函数时(重载)，会根据最终输入的参数来决定调用哪个函数。
#       双分派顾名思义，即最终的操作决定于两个接收者的类型，
#       在本例中，药品和工作人员互相调用了对方（药品的accept和工作人员的visit中，对方都是参数），就是双分派的一种应用。
#   Python原生是不支持静态分派的，因而也不直接支持更高层次的分派。
#   访问者模式实现的分派，是一种动态双分派（重写）。
#   但这并不妨碍Python通过访问者模式实现一种基于类的“双分派效果”。
#   Python多分派可以参考David Mertz 博士的一篇文章：可爱的Python：多分派—用多元法泛化多样性。
#
#   优点：
#       1、将不同的职责分开，符合单一职责原理
#       2、拓展非常简单，加减元素和访问者都非常简单
#
#   缺点：
#       1、访问者得知了元素细节，与最小隔离原则相悖；
#       2、元素变更依旧可能引起Visitor的修改。
#
#   应用：
#       1、要遍历不同的对象，根据对象进行不同的操作的场景；
#          或者一个对象被多个不同对象顺次处理的情况，可以考虑使用访问者模式。
#          如：除本例外，报表生成器也可以使用访问者模式实现，报表的数据源由多个不同的对象提供，每个对象都是Visitor，报表这个Element顺次Accept各访问者完善并生成对象。


###### 药房业务系统 ######
# 假设一个药房，有一些大夫，一个药品划价员和一个药房管理员，它们通过一个药房管理系统组织工作流程。
# 大夫开出药方后，药品划价员确定药品是否正常，价格是否正确；
# 通过后药房管理员进行开药处理。
# 该系统可以如何实现？
# 最简单的想法，是分别用一个一个if…else…把划价员处理流程和药房管理流程实现，这样做的问题在于，扩展性不强，
# 而且单一性不强，一旦有新药的加入或者划价流程、开药流程有些变动，会牵扯比较多的改动。
class Medicine:
    name = ""
    price = 0.0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def accept(self, visitor):
        pass


# 抗生素
class Antibiotic(Medicine):
    def accept(self, visitor):
        visitor.visit(self)


# 感冒药
class Coldrex(Medicine):
    def accept(self, visitor):
        visitor.visit(self)


class Visitor:
    name = ""

    def setName(self, name):
        self.name = name

    def visit(self, medicine):
        pass


# 药品划价员
class Charger(Visitor):
    def visit(self, medicine):
        print("CHARGE: %s lists the Medicine %s. Price:%s " % (self.name, medicine.getName(), medicine.getPrice()))


# 药品管理员
class Pharmacy(Visitor):
    def visit(self, medicine):
        print("PHARMACY:%s offers the Medicine %s. Price:%s" % (self.name, medicine.getName(), medicine.getPrice()))


class ObjectStructure:
    pass


# 处方
class Prescription(ObjectStructure):
    medicines = []

    def addMedicine(self, medicine):
        self.medicines.append(medicine)

    def rmvMedicine(self, medicine):
        self.medicines.append(medicine)

    def visit(self, visitor):
        for medc in self.medicines:
            medc.accept(visitor)


if __name__ == "__main__":
    yinqiao_pill = Coldrex("Yinqiao Pill", 2.0)
    penicillin = Antibiotic("Penicillin", 3.0)
    doctor_prsrp = Prescription()
    doctor_prsrp.addMedicine(yinqiao_pill)
    doctor_prsrp.addMedicine(penicillin)
    charger = Charger()
    charger.setName("Doctor Strange")
    pharmacy = Pharmacy()
    pharmacy.setName("Doctor Wei")
    doctor_prsrp.visit(charger)
    doctor_prsrp.visit(pharmacy)
