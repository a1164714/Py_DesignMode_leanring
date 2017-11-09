# 策略模式定义：定义一组算法，将每个算法都封装起来，并使他们之间可以互换。
#   以上述例子为例，customer类扮演的角色（Context）直接依赖抽象策略的接口，在具体策略实现类中即可定义个性化的策略方式，且可以方便替换。
#
# 优点：
#       1、各个策略可以自由互换。
#       2、减少代码冗余
#       3、拓展性优秀，移植方便，使用灵活。
#
# 缺点：
#       1、项目比较庞大时，策略比较多，不便于维护
#       2、策略的使用方必须知道有哪些策略，才能决定使用哪一个策略，这与迪米特法则是相违背的。
#
# 应用：
#       1、算法策略比较经常地需要被替换时，可以使用策略模式。
#               如现在超市前台，会常遇到刷卡、某宝支付、某信支付等方式，就可以参考策略模式。
#
#
####### 客户消息通知 #######
# 假设某司维护着一些客户资料，需要在该司有新产品上市或者举行新活动时通知客户。现通知客户的方式有两种：短信通知、邮件通知。
class Customer:
    customer_name = ""
    snd_way = ""  # 向客户发送信息的方式
    info = ""
    phone = ""
    email = ""

    def setPhone(self, phone):
        self.phone = phone

    def setEmail(self, mail):
        self.email = mail

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email

    def setInfo(self, info):
        self.info = info

    def setName(self, name):
        self.customer_name = name

    def setBrdWay(self, snd_way):
        self.snd_way = snd_way

    def sndMsg(self):
        self.snd_way.send(self.info)


# 发送方式构建
class msgSender:
    dst_code = ""

    def setCode(self, code):
        self.dst_code = code

    def send(self, info):
        pass


class emailSender(msgSender):
    def send(self, info):
        print("EMAIL_ADDRESS:%s EMAIL:%s" % (self.dst_code, info))


class textSender(msgSender):
    def send(self, info):
        print("TEXT_CODE:%s TEXT_INFO:%s" % (self.dst_code, info))


if __name__ == "__main__":
    customer_x = Customer()
    customer_x.setName("CUSTOMER_X")
    customer_x.setPhone("10023456789")
    customer_x.setEmail("customer_x@xmail.com")
    customer_x.setInfo("Welcome to our new party!")
    text_sender = textSender()
    text_sender.setCode(customer_x.getPhone())
    customer_x.setBrdWay(text_sender)
    customer_x.sndMsg()
    mail_sender = emailSender()
    mail_sender.setCode(customer_x.getEmail())
    customer_x.setBrdWay(mail_sender)
    customer_x.sndMsg()
