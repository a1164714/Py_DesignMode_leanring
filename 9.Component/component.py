# 定义：组合模式也叫部分-整体模式，将对象组合成树结构以表示“部分”和“整体”的层次结构，使得用户对单个对象和组合对象的使用具有一致性

# 优点：
#       1、节点增加和减少自由方便
#       2、所有节点（根节点、分支节点和叶节点）调用节点或节点群非常方便
#
# 缺点：
#       1、由于叶子节点和分支节点直接使用了实现类，大大限制了接口的影响范围；若节点变更对系统影响太大
#
# 应用：
#       1、维护部分与整体的逻辑关系，或者动态调用整体或部分的功能接口，可以考虑使用组合模式。
#           例如，非常多的操作系统（如Linux）都把文件系统设计成树形结构，再比如说分布式应用中借助Zookeeper，也可以组织和调用分布式集群中的结点功能。

########## 公司结构组织(树状) #######
class Company:  # 接口
    name = ''

    def __init__(self, name):
        self.name = name

    def add(self, company):
        pass

    def remove(self, company):
        pass

    def display(self, depth):
        pass

    def listDuty(self):
        pass


class ConcreteCompany(Company):
    childrenCompany = None

    def __init__(self, name):
        Company.__init__(self, name)
        self.childrenCompany = []

    def add(self, company):
        self.childrenCompany.append(company)

    def remove(self, company):
        self.childrenCompany.remove(company)

    def display(self, depth):
        print('-' * depth + self.name)
        for component in self.childrenCompany:
            component.display(depth + 1)

    def listDuty(self):
        for component in self.childrenCompany:
            component.listDuty()


class HRDepartment(Company):
    def __init__(self, name):
        Company.__init__(self, name)

    def display(self, depth):
        print('-' * depth + self.name)

    def listDuty(self):  # 履行职责
        print('%s\t Enrolling & Transfering management.' % self.name)


class FinanceDepartment(Company):
    def __init__(self, name):
        Company.__init__(self, name)

    def display(self, depth):
        print("-" * depth + self.name)

    def listDuty(self):  # 履行职责
        print('%s\tFinance Management.' % self.name)


class RdDepartment(Company):
    def __init__(self, name):
        Company.__init__(self, name)

    def display(self, depth):
        print("-" * depth + self.name)

    def listDuty(self):
        print("%s\tResearch & Development." % self.name)

if __name__=="__main__":
    root = ConcreteCompany('HeadQuarter')
    root.add(HRDepartment('HQ HR'))
    root.add(FinanceDepartment('HQ Finance'))
    root.add(RdDepartment("HQ R&D"))

    comp = ConcreteCompany('East Branch')
    comp.add(HRDepartment('East.Br HR'))
    comp.add(FinanceDepartment('East.Br Finance'))
    comp.add(RdDepartment("East.Br R&D"))
    root.add(comp)

    comp1 = ConcreteCompany('Northast Branch')
    comp1.add(HRDepartment('Northeast.Br HR'))
    comp1.add(FinanceDepartment('Northeast.Br Finance'))
    comp1.add(RdDepartment("Northeast.Br R&D"))
    comp.add(comp1)

    comp2 = ConcreteCompany('Southeast Branch')
    comp2.add(HRDepartment('Southeast.Br HR'))
    comp2.add(FinanceDepartment('Southeast.Br Finance'))
    comp2.add(RdDepartment("Southeast.Br R&D"))
    comp.add(comp2)

    root.display(1)

    root.listDuty()