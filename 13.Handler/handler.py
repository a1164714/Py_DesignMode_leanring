# 责任链模式定义：使多个对象都有机会处理请求，从而避免了请求的发送者和接收者之间的耦合关系。将这些对象连成一条链，并沿着这条链传递该请求，直到有对象处理它为止。
#  责任链模式中的应该只有一个处理者，也就是说，本例中的“最终批准”为该对象所谓的“请求处理”。
#
# 优点：
#       1、将请求者和处理者分离，请求者不需要知道请求最终被谁处理了
#
# 缺点：
#       1、责任链太长可能出现性能问题
#       2、责任链太长可能出现调试问题，出了问题，很难定位到错误
#
# 应用：
#       1、若一个请求可能由一个对请求有链式优先级的处理群所处理时，可以考虑责任链模式。
#           除本例外，银行的客户请求处理系统也可以用责任链模式实现（VIP客户和普通用户处理方式当然会有不同）。
#

###### 请假系统 #####
#   员工若想要请3天以内（包括3天的假），只需要直属经理批准就可以了；
#   如果想请3-7天，不仅需要直属经理批准，部门经理需要最终批准；
#   如果请假大于7天，不光要前两个经理批准，也需要总经理最终批准。
class manager():
    successor = None
    name = ''

    def __init__(self, name):
        self.name = name

    def setSuccessor(self, successor):
        self.successor = successor

    def handleRequest(self, request):
        pass


class lineManager(manager):
    def handleRequest(self, request):
        if request.requestType == 'DaysOff' and request.number <= 3:
            print('%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number))
        else:
            print('%s:%s Num:%d Accepted CONTINUE' % (self.name, request.requestContent, request.number))
            if self.successor != None:
                self.successor.handleRequest(request)


class departmentManager(manager):
    def handleRequest(self, request):
        if request.requestType == 'DaysOff' and request.number <= 7:
            print('%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number))
        else:
            print('%s:%s Num:%d Accepted CONTINUE' % (self.name, request.requestContent, request.number))
            if self.successor != None:
                self.successor.handleRequest(request)


class generalManager(manager):
    def handleRequest(self, request):
        if request.requestType == 'DaysOff':
            print('%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number))


class request():
    requestType = ''
    requestContent = ''
    number = 0

if  __name__=="__main__":
    line_manager = lineManager('LINE MANAGER')
    department_manager = departmentManager('DEPARTMENT MANAGER')
    general_manager = generalManager('GENERAL MANAGER')
    # 设置上属
    line_manager.setSuccessor(department_manager)
    department_manager.setSuccessor(general_manager)

    # 所有的责任中从最低开始
    req = request()
    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 1 day off'
    req.number = 1
    line_manager.handleRequest(req)

    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 5 days off'
    req.number = 5
    line_manager.handleRequest(req)

    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 10 days off'
    req.number = 10
    line_manager.handleRequest(req)