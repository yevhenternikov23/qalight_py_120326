
def add(x, y):
    return x + y

def diff(x, y):
    return x - y

def calculate(func, x, y):
    return func(x, y)

result_a = calculate(add, 4, 6)
result_b = calculate(diff, 4, 6)
print(result_a, result_b)


def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello


greet = greeting("Atlantis")
print(greet())


def make_title(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        new_args = []
        for a in args:
            if a.islower():
                new_args.append(a.title())
            else:
                new_args.append(a)
        result = func(*new_args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@make_title
def say_hello(name):
    print(f"Привіт, {name}!")

say_hello("alex")
say_hello("Natalia")


class MyClass:
    count = 0

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.count += 1
        return instance

    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x
    
    @classmethod
    def my_class_method(cls):
        cls.count = 1
    
    @staticmethod
    def lets_dance(a):
        return f"{a} Dancing!"

my_item = MyClass(1)
print("1", my_item.count)
# my_item.count = 2
my_item_2 = MyClass(7)
my_item_3 = MyClass(567)

print(my_item_3.count)

print("2", my_item.count)

print(MyClass.lets_dance("Yevheniy"))
print(my_item_3.lets_dance("alex"))