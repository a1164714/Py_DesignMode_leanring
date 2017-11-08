# encoding=utf8
import threading
import time

# 应用：
# 1、生成全局唯一序列号
# 2、访问全局复用的唯一资源，如磁盘、总线等
# 3、单个对象占用资源过多，如数据库连接等
# 4、系统全局统一管理，如系统资源管理器等
# 5、网站计数器

# 优点：
# 1、全局只有一个实例，节约内存空间
# 2、全局只有一个接入点，更好得地进行数据同步
# 3、单例常驻内存，减小系统开销

# 缺点：
# 1、拓展困难
# 2、赋予单例太多职责，违反单一职责原则
# 3、单例某些情况会导致“资源瓶颈”

# use method '_new_' to implement singleton
class Singleton(object):  # 抽象单例
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

### 总线系统
# 总线
class Bus(Singleton):
    lock = threading.RLock()

    def sendData(self, data):
        self.lock.acquire()
        time.sleep(3)
        print("Sending Signal Data...", data)
        self.lock.release()


# 线程对象，为更加说明单例的含义，这里将Bus对象实例化写在run里
class VisitEntity(threading.Thread):
    my_bus = ""
    name = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def run(self):
        self.my_bus = Bus()
        self.my_bus.sendData(self.name)


if __name__ == '__main__':
    for i in range(3):
        print("Entity %d begin to run..." %i)
        my_entity = VisitEntity()
        my_entity.setName("Entity_" + str(i))
        my_entity.start()
