# 模板模式定义如下：定义一个操作中的算法的框架，而将一些步骤延迟到子类中，使得子类可以不改变一个算法的结构即可重新定义该算法的某些特定的步骤。
#                   子类实现的具体方法叫作基本方法，实现对基本方法高度的框架方法，叫作模板方法。
#
# 优点：
#       1、可变部分可以充分拓展，不变部分的步骤可以充分封装
#       2、提供公共代码，减少冗余代码，便于维护
#       3、具体过程可以定制，总体流程容易控制
#
# 缺点：
#       1、模板模式在抽象类中定义了子类的方法，即子类对父类产生了影响，部分影响了代码的可读性。
#
# 应用场景：
#       1、某超类的子类中有公有的方法，并且逻辑基本相同，可以使用模板模式。
#           如：必要时可以使用钩子方法约束其行为。具体如本节例子；
#       2、比较复杂的算法，可以把核心算法提取出来，周边功能在子类中实现。
#           如：机器学习中的监督学习算法有很多，如决策树、KNN、SVM等，
#                   但机器学习的流程大致相同，都包含输入样本、拟合（fit）、预测等过程，
#                   这样就可以把这些过程提取出来，构造模板方法，并通过钩子方法控制流程。
#
#### 股票查询客户端 #####
# 根据股票代码来查询股价分为如下几个步骤：登录、设置股票代码、查询、展示。

# 虚拟股票查询器（客户端）
class StockQueryDevice():
    stock_code = "0"
    stock_price = 0.0

    def login(self, usr, pwd):
        pass

    def setCode(self, code):
        self.stock_code = code

    def queryPrice(self):
        pass

    def showPrice(self):
        pass

    # 模板模式
    def operateQuery(self, usr, pwd, code):
        if not self.login(usr, pwd):
            return False
        self.setCode(code)
        self.queryPrice()
        self.showPrice()
        return True


class WebAStockQueryDevice(StockQueryDevice):
    def login(self, usr, pwd):
        if usr == "myStockA" and pwd == "myPwdA":
            print("Web A:Login OK... user:%s pwd:%s" % (usr, pwd))
            return True
        else:
            print("Web A:Login ERROR... user:%s pwd:%s" % (usr, pwd))
            return False

    def queryPrice(self):
        print("Web A Querying...code:%s " % self.stock_code)
        self.stock_price = 20.00

    def showPrice(self):
        print("Web A Stock Price...code:%s price:%s" % (self.stock_code, self.stock_price))


class WebBStockQueryDevice(StockQueryDevice):
    def login(self, usr, pwd):
        if usr == "myStockB" and pwd == "myPwdB":
            print("Web B:Login OK... user:%s pwd:%s" % (usr, pwd))
            return True
        else:
            print("Web B:Login ERROR... user:%s pwd:%s" % (usr, pwd))
            return False

    def queryPrice(self):
        print("Web B Querying...code:%s " % self.stock_code)
        self.stock_price = 30.00

    def showPrice(self):
        print("Web B Stock Price...code:%s price:%s" % (self.stock_code, self.stock_price))

# 每次操作，都会调用登录，设置代码，查询，展示这几步，是不是有些繁琐？
if  __name__=="__main__":
    # web_a_query_dev=WebAStockQueryDevice()
    # web_a_query_dev.login("myStockA","myPwdA")
    # web_a_query_dev.setCode("12345")
    # web_a_query_dev.queryPrice()
    # web_a_query_dev.showPrice()

    # 使用模板改进代码
    web_a_query_dev = WebAStockQueryDevice()
    web_a_query_dev.operateQuery("myStockA", "myPwdA", "12345")