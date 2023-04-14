class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def show_attributes(obj):
    print(obj.__dict__)


show_attributes(MyClass(1, 2))