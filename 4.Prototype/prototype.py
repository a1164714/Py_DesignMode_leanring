from copy import deepcopy, copy


# 定义: 用原型实例指定创建对象的种类，并且通过复制这些原型创建新的对象。
# 需要注意一点的是，进行clone操作后，新对象的构造函数没有被二次执行，新对象的内容是从“内存”里直接拷贝的。

# 优点：
#       性能极佳，直接拷贝比在内存里直接新建实例节省不少的资源；
#       简化对象创建，同时避免了构造函数的约束，不受构造函数的限制直接复制对象，是优点，也有隐患，这一点还是需要多留意一些。
# 缺点：
# 1、深拷贝和浅拷贝的使用需要事先考虑周到；
# 2、某些编程语言中，拷贝会影响到静态变量和静态函数的使用。


######## 画图系统 ###########
class simpleLayer:
    background = [0, 0, 0, 0]
    content = "blank"

    def getContent(self):
        return self.content

    def getBackgroud(self):
        return self.background

    def paint(self, painting):
        self.content = painting

    def setParent(self, p):
        self.background[3] = p

    def fillBackground(self, back):
        self.background = back

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


if __name__ == "__main__":
    dog_layer = simpleLayer()
    dog_layer.paint("Dog")
    dog_layer.fillBackground([0, 0, 255, 0])
    print("Original Background:", dog_layer.getBackgroud())
    print("Original Painting:", dog_layer.getContent())
    another_dog_layer = dog_layer.deep_clone()
    another_dog_layer.setParent(128)
    another_dog_layer.paint("Puppy")
    print("Original Background:", dog_layer.getBackgroud())
    print("Original Painting:", dog_layer.getContent())
    print("Copy Background:", another_dog_layer.getBackgroud())
    print("Copy Painting:", another_dog_layer.getContent())
