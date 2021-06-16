import inspect


# class Thing_old:

#     def __init__(self, x):
#         self.__x = x

#     def getx(self):
#         return self.__x

#     @property
#     def setx(self, x):
#         self.__x = x


class property_new:
    def __init__(self, getter, setter=None):
        self.__name__ = getter.__name__
        self.__get = getter
        self.__set = setter

    def __get__(self, instance, owner=None):
        return self.__get(instance)

    def __set__(self, instance, value):
        self.__set(instance, value)

    def setter(self, setter):
        self.__set = setter
        return self


class Thing:

    def __init__(self, x):
        self.__x = x

    @property_new
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x


def main():
    thing = Thing(5)
    print(thing.x)
    thing.x = 10
    print(thing.x)
    return 0


if __name__ == "__main__":
    main()
