class SingleTon(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance


s1 = SingleTon()
s2 = SingleTon()
print(id(s1))
print(id(s2))