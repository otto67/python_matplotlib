
# Module for exploring the features of Python classes
class First:
    _priv1 = 3
    _priv2 = 6
    _priv3 = 7

    def __init__(self, a=1, b=1, c=1):
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @staticmethod
    def firstStaticMet():
        return First._priv1 + First._priv2 + First._priv3

    @classmethod
    def firstFactoryMethod(cls):
        return First(cls._priv1, cls._priv2, cls._priv3)

    def __call__(self, *args, **kwargs):
        print("Who called ?", '-'.join(*args), " ", dict(**kwargs))
        print(args, kwargs)

    def __add__(self, other):
        x = self.a + other.a
        y = self.b + other.b
        z = self.c + other.c
        return First(x, y, z)

    def __sub__(self, other):
        x = self.a - other.a
        y = self.b - other.b
        z = self.c - other.c
        return First(x, y, z)

    def __mul__(self, other):
        x = self.a * other.a
        y = self.b * other.b
        z = self.c * other.c
        return First(x, y, z)

    def __eq__(self, other):
        if (self.a == other.a) and (self.b == other.b) and (self.c == other.c):
            return True
        else:
            return False

class Second(First):

        _priv1 = 11
        _priv2 = 22
        _priv3 = 33

        def __init__(self, a=1, b=1, c=1, d=1, e=1):
            super().__init__(a, b, c)
            self._d = d
            self._e = e

        @property
        def d(self):
            return self._d

        @property
        def e(self):
            return self._e

        def __add__(self, other):

            if not isinstance(other, First):
                return Second(self.a, self.b, self.c, self.d, self.e)

            x = self.a + other.a
            y = self.b + other.b
            z = self.c + other.c

            if not isinstance(other, Second):
                return Second(x, y, z, self.d, self.e)

            d = self.d + other.d
            e = self.e + other.e
            return Second(x, y, z, d, e)

        @staticmethod
        def secondStaticMet():
            return Second._priv1 + Second._priv2 + Second._priv3

        @classmethod
        def secondFactoryMethod(cls):
            return Second(cls._priv1, cls._priv2, cls._priv3)


def myprint(o):
    print("Class ", o.__class__,"Values are :", o.a, " ", o.b, " ", o.c)

if __name__ == "__main__":

    print("Sum is ", First.firstStaticMet())

    f = First()
    myprint(f)
    g = First(2, 3, 4)
    myprint(g)
    h = f + g
    myprint(h)
    i = f - g
    myprint(i)
    j = g*h
    myprint(j)
    k = First()
    print(f == k)
    print(f == j)

    a = First.firstFactoryMethod()
    myprint(a)

    b = Second()
    myprint(b)


    c = Second.secondFactoryMethod()
    myprint(c)

    print("Sum is ", Second.secondStaticMet())

    d = b + b
    myprint(d)
    e = f + b
    myprint(e)

    print(type(f))
    print(type(d))
    print(isinstance(f, First))
    print(isinstance(d, First))
    print(isinstance(d, Second))
    print(isinstance(f, Second))

    c= { 'a': 't' }
    c['b'] = 'u'
    f(['This', 'is', 'a', 'list','of', 'arguments'], hello='a', hallo='b')
