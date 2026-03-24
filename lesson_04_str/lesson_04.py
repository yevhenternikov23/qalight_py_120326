
my_first_str = "Привіт!"
print(my_first_str[0])
print(my_first_str[1])
print(my_first_str[2])
print(my_first_str[-1])
print(my_first_str[-2])

print(my_first_str[1:4]) #slices

sequence = "abcdefghij"
result = sequence[1:9:2]  # Вибираємо "bdfh"
print(result)

print("my_first_str", len(my_first_str))
print("sequence", len(sequence))

for char in sequence:
    print(char)

print("==")

goal = "гол"
sum_goal = goal + goal
print(sum_goal)
mul_goal = goal * 3
print(mul_goal)

result_join = ", ".join(["a", "aaa", goal, mul_goal])
print(result_join)

my_long_str = "Якщо не вказати конкретний роздільник, `split()` використовує пробіли"
parts = my_long_str.split()
print(parts)

line = "apple,orange,banana,grape"
parts = line.split(',')
print(parts)

line = "apple,orange,banana,grape"
parts = line.split(',', 2)
print(parts)

line = "Hello, World!"

print(line.startswith("Hello"))
# Перевірка, чи рядок починається з певної підстрічки
if line.startswith("Hello"):
    print("Рядок починається з 'Hello'")
else:
    print("Рядок не починається з 'Hello'")

print(line.endswith("World!"))
# Перевірка, чи рядок закінчується певною підстрічкою
if line.endswith("World!"):
    print("Рядок закінчується на 'World!'")
else:
    print("Рядок не закінчується на 'World!'")

print(sequence.startswith("a"))
print(sequence.startswith("b"))
print(sequence.startswith("ab"))
print(sequence.startswith("abcdefghij"))

chars = "HELLO"
print(chars.isupper())
lower = chars.lower()
print(lower)

chars_2 = "hello"
print(chars_2.islower())

chars_3 = "Hello"
print(chars_3.istitle())
upper_3 = chars_3.upper()
print(upper_3)

fairy_tales = "жилsи були дід та баба і булsа у них Курочка Рsябsа"

print(fairy_tales.capitalize())
print(fairy_tales.title())
print(fairy_tales.title().swapcase())

index = fairy_tales.lower().find("курочка")
print(index)

start = fairy_tales.find("бул")
print(start)
second = fairy_tales.find("бул", start + 1)
print(second)
thrd = fairy_tales.find("бул", second + 1)
print(thrd)

repl_str = fairy_tales.replace("бул", "бумбум")
print(repl_str)

repl_str = fairy_tales.replace("s", "")
print(repl_str)

line_for_strip = "    Привіт, світ!    "
clean_str = line_for_strip.strip()
print(f"|{clean_str}|")
clean_str_l = line_for_strip.lstrip()
print(f"|{clean_str_l}|")
clean_str_r = line_for_strip.rstrip()
print(f"|{clean_str_r}|")


line_for_strip_2 = "..zzz   Привіт, світ!   zzzzz...."
clean_str = line_for_strip_2.strip(".").strip("z").strip()
print(f"|{clean_str}|")

str_list = ["apple", "orange", "banana"]

# Об'єднання рядків зі списку за допомогою роздільника ','
joined_strs = ','.join(str_list)
print(joined_strs)

my_data = 122 #input("Веедіть ваш вік:")
print(my_data)

my_data_str = "123"
my_int = int(my_data_str)
print(my_int, type(my_int))

my_data_str_2 = "123.999"
my_flt = float(my_data_str_2)
print(my_flt, type(my_flt))
print(int(my_flt))
print(round(my_flt, 0))

my_bool_str = "True"
my_bool_str_2 = "False"
print(bool(my_bool_str))
print(bool(my_bool_str_2))
print(bool("")) # False == "", '', "''", """""", 0, {}, [], (), set()

name = "Vasya"
age = 25

out_str = f"Hello, {name}, your age is {age}"
print(out_str)

а = 5
б = 10
рядок = f"Сума чисел {а} та {б} дорівнює {а + б}."
print(рядок)
