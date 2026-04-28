
def simple_generator():
    yield 343
    yield "asdsad"
    yield 76

gen = simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))


def my_generator(n):
    # Ініціалізуємо лічильник
    value = 1
    # Цикл виконується доти, доки лічильник не стане менше n
    while value <= n:
        # Повертаємо поточне значення лічильника
        yield value
        # Збільшуємо лічильник
        value += 1

for value in my_generator(7):
    # Виводимо кожне значення, отримане від генератора
    print(value)

generator = my_generator(3)
print(next(generator))  # 1
print(next(generator))  # 2
print(next(generator))  # 3
print(*generator)


numbers = [1, 2, 3, 4, 5]
sq_iter = map(lambda x: x * 2, numbers)
print(sq_iter)
print(next(sq_iter))
print(*sq_iter)
# print(next(sq_iter))


names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zip_it = zip(names, ages)

print(next(zip_it))
cmd = dict(i for i in zip_it)
print(cmd)