import random
import string

def basic():
    pass

#print(basic())

#print(print())

def print_song():
    """Друкує пісню"""
    print("Ой у лузі червона калина похилилася")
    print("Чогось наша славна Україна зажурилася")

print_song()

def get_song():
    """Отримай пісню"""
    return "А ми тую червону калину підймемо \n" \
        "А ми нашу славну Україну..."

gs = get_song()
print(gs)
print(len(gs), type(gs))

def hello(name):
    return f"{name} hello!"

print(hello("Viacheslav"))

# print(hello())  TypeError

def add(a: int, b: int) -> int:
    """Add a plus b
    
    Return:
        a + b value
    """
    return a + b

sum_ab = add(2, 3)
print("ADD", sum_ab, type(sum_ab))

def greet(name: str, greeting: str = "Привіт"):
    """
    Функція виводить привітання для заданого імені.

    :param name: Ім'я для привітання
    :param greeting: Привітання (за замовчуванням "Привіт")
    """
    out = f"{greeting}, {name.title()}!"
    print(out)
    # return out

greet("Юрій")
greet("Оксана", "Доброго дня")
greet("саня", "хало")
print(greet(""))
greet("привітання", "Юрій")

greet(greeting="Hello", name="Genna")

def calculate_price(base_price: float, discount=0.0, tax=0.2) -> float:
    return base_price * (1 - discount) * (1 + tax)

base_price = 100 # float(input("base_price "))
calc = calculate_price(base_price)
print(calc)
calc_2 = calculate_price(base_price, 0.1)
print("disc", calc_2)
calc_3 = calculate_price(base_price, 0.05, 0)
print("disc", calc_3)

def generate_password(length=8, use_digits=True, use_special=False):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%"
    # out = ""
    # for _ in range(length):
    #     char = random.choice(chars)
    #     out += char
    # return out
    return ''.join(random.choice(chars) for _ in range(length))

print(generate_password())

def print_args(*args):
    for arg in args:
        print(arg)
print("=============")
print_args(1)
print("=============")
print_args(1, "hello")
print("=============")
print_args(1, "hello", None)
print("=============")
print_args(1, "hello", 3.14, [1, 2, 3])


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Приклад виклику функції
print_kwargs(name="John", age=25, city="New York")

def describe_person(name, age, country="Unknown"): # 
    print(f"{name} is {age} years old and is from {country}.")

describe_person("Alice", 30, )  # "Canada"Alice is 30 years old and is from Unknown.
describe_person("Bob", 25, country="USA")  # Bob is 25 years old and is from USA.
# describe_person("Charlie", country="Canada", 28)
describe_person("Charlie", country="Canada", age=28)

ladd = lambda x, y: x + y

print(ladd(2, 4))

square = lambda x: x**2

print(square(5))

print("============="*6)


print(all([1, 2, -4]))
print(all([1, 2, 0]))


print(any([1,2,3]))
print(any([0,2,0]))
print(any([0,0,0]))

byte_array = bytearray(b'Hello, World!')
print(id(byte_array))
byte_array[0] = 37  # bytearray змінний, тож 0 елемент
                    # змінюється на символ з кодом 37 == %
print(byte_array.decode('utf-8'))   # %ello, World!
print(id(byte_array))

print(chr(1111), chr(44), chr(37))

my_dict = dict(a="a", b=[1,2])
print(my_dict)

value1 = "abc"
value2 = "DER"
formatted_string = "Some text {} and {}.".format(value1, value2)
print(formatted_string)

hello_my = "hello"  
print(id(hello_my))
hello_my = "ferer"
print(id(hello_my))


print(type("hello"))
x = 5
print(isinstance(x, int))
print(isinstance(x, str))
print(isinstance(x, (float, int)))


print(len("len"))

print(max([3, 1, 4]))
print(min([3, 1, 4]))

print(pow(3, 3))
print(3**3)


print(list(reversed([10, 2, 4])))

print(round(2.60))
print(round(2.40))

print(sorted([2, 4, 2, 3, 7]))
a = [2, 4, 2, 3, 7]
print(a.sort())

print(str(123))

print(sum([1, 2, 3, -2, -3, -1]))


words = ["яблуко", "апельсин", "банан", "груша", "слива"]
# Сортування за довжиною рядків
sorted_words = sorted(words, key=len)
print(sorted_words)
