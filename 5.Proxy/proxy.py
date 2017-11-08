# 定义: 为某个对象提供代理，以控制对此对象的访问和控制。
# 代理模式在使用过程中，应尽量对抽象主题类进行代理，而尽量不要对加过修饰和方法的子类代理。
# 如上例中，如果有一个xServer继承了Server，并新加了方法xMethod，xServer的代理应以Server为主题进行设计，而尽量不要以xServer为主题，以xServer为主题的代理可以从ServerProxy继承并添加对应的方法。

# 代理模式是AOP的重要实现手段，JAVA则经常提到动态代理，但python很少提到。AOP还可以使用装饰器模式来实现。

# 优点：
#       1、职责简单：非本职责的事务由代理完成
#       2、拓展性强：面对主题对象可能会有的改变，代理模式在不改变对外接口的情况下，可以实现最大程度的扩展；
#       3、保证主题对象的处理逻辑：代理可以通过检查参数来保证主题对象的处理逻辑输入在理想范围内
#
#  缺点：
#       1、会降低整体业务的处理效率和速度
#
#应用场景：
#       1、针对某特定对象进行功能和增强性拓展。如：IP防火墙、远程访问代理等
#       2、对主题对象进行保护。如：大流量代理、安全代理等
#       3、减轻主题对象负载。如权限代理等

info_struct = dict()
info_struct["addr"] = 10000
info_struct["content"] = ""


class Server:
    content = ""

    def recv(self, info):
        pass

    def send(self, info):
        pass

    def show(self):
        pass


class InfoServer(Server):
    def recv(self, info):
        self.content = info
        return "recv info"

    def send(self, info):
        pass

    def show(self):
        print("SHOW:%s" % self.content)


class ServerProxy:
    pass


class InfoServerProxy(ServerProxy):
    server = ""

    def __init__(self, server):
        self.server = server

    def recv(self, info):
        return self.server.recv(info)

    def show(self):
        self.server.show()


class WhiteInfoServerProxy(InfoServerProxy):
    white_list = []

    def recv(self, info):
        try:
            assert type(info) == dict
        except:
            return "info structure is not correct"
        addr = info.get("addr", 0)
        if not addr in self.white_list:
            return "Your address is not in the white list."
        else:
            content = info.get("content", "")
            return self.server.recv(content)

    def addWhite(self, addr):
        self.white_list.append(addr)

    def rmvWhite(self, addr):
        self.white_list.remove(addr)

    def clearWhite(self):
        self.white_list.clear()


if __name__ == "__main__":
    info_struct = dict()
    info_struct["addr"] = 10010
    info_struct["content"] = "Hello World!"
    info_server = InfoServer()
    info_server_proxy = WhiteInfoServerProxy(info_server)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()
    info_server_proxy.addWhite(10010)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()
