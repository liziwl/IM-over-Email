class SingletonDecorator:
    def __init__(self,klass):
        self.klass = klass
        self.instance = None
    def __call__(self,*args,**kwds):
        if self.instance == None:
            self.instance = self.klass(*args,**kwds)
        return self.instance


class MagicClass: pass


MagicClass = SingletonDecorator(MagicClass)


if __name__ == '__main__':
    magic = MagicClass()
    magic.something = "Hello world"

    magic2 = MagicClass()
    print(magic2.something)