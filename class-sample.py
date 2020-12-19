# 普通にclass作りたい時はobjectを継承して作る
class Hoge(object):
    default_value = 'hogehoge'

    def __init__(self, value=None):
        if value:
            self.value = value
        else:
            self.value = self.default_value

    def get_value(self):
        return self.value

hoge = Hoge('foo')
print(hoge.get_value())

class BaseClass(object):
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

# 継承するclassは()に書く
class SubClass(BaseClass):
    def __init__(self, value):
        value = value * 2
        super(SubClass, self).__init__(value)

hoge = SubClass(10)
print(hoge.get_value())
