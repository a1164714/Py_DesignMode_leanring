# 门面模式定义：要求一个子系统的外部与其内部的通信必须通过一个统一的对象进行。
#   门面模式提供一个高层次的接口，使得子系统更易于使用。
#   门面模式注重“统一的对象”，也就是提供一个访问子系统的接口。
#   门面模式与之前说过的模板模式有类似的地方，都是对一些需要重复方法的封装。
#   但从本质上来说，是不同的。模板模式是对类本身的方法的封装，其被封装的方法也可以单独使用；
#   而门面模式，是对子系统的封装，其被封装的接口理论上是不会被单独提出来用的。
#
# 优点：
#       1、减少了系统之间的相互依赖，提高了系统的灵活；
#       2、提高了整体系统的安全性：封装起的系统对外的接口才可以用，隐藏了很多内部接口细节，若方法不允许使用，则在门面中可以进行灵活控制。
#
# 缺点：
#       1、门面模式的缺点在于，不符合开闭原则，一旦系统成形后需要修改，几乎只能重写门面代码，
#           这比继承或者覆写等方式，或者其它一些符合开闭原则的模式风险都会大一些。
#
# 应用场景：
#       1、为一个复杂的子系统提供一个外界访问的接口。这类例子是生活还是蛮常见的，例如电视遥控器的抽象模型，电信运营商的用户交互设备等；
#       2、需要简化操作界面时。例如常见的扁平化系统操作界面等，在生活中和工业中都很常见。

####### 火灾警报器 ########
class AlarmSensor:
    def run(self):
        print("Alarm Ring...")


class WaterSprinker:
    def run(self):
        print("Spray Water...")


class EmergencyDialer:
    def run(self):
        print("Dial 119...")

# 警报门面
class EmergencyFacade:
    def __init__(self):
        self.alarm_sensor = AlarmSensor()
        self.water_sprinker = WaterSprinker()
        self.emergency_dialer = EmergencyDialer()

    def runAll(self):
        self.alarm_sensor.run()
        self.water_sprinker.run()
        self.emergency_dialer.run()


if __name__=="__main__":
    # alarm_sensor = AlarmSensor()
    # water_sprinker = WaterSprinker()
    # emergency_dialer = EmergencyDialer()
    # alarm_sensor.run()
    # water_sprinker.run()
    # emergency_dialer.run()

    emergency_facade=EmergencyFacade()
    emergency_facade.runAll()