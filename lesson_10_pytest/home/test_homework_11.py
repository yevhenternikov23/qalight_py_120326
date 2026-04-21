"""
Тести для файлу tasks.py
Запуск: pytest test_tasks.py
"""
from functions_for_test import *

"""
📝 Завдання 1. Перевірка додавання чисел 
Напиши тест на функцію add(a, b), яка повертає суму двох чисел. 
Створи тест, який перевіряє кілька випадків: додавання додатних, від’ємних і нуля.
"""
def test_add(a, b):
    # TODO: додай тести для функції add
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-4, -4) == -8
    assert add(7, 0) == 7
    assert add(0, 3) == 3

"""
📝 Завдання 2. Перевірка парності 
Функція is_even(n) повертає True, якщо число парне, інакше False. 
Напиши тести для кількох чисел: парних, непарних, від’ємних.
"""
def test_is_even(n):
    # TODO: додай тести для функції is_even
    if n % 2 == 0:
        return True
    
def test_is_even():
    assert is_even(4) is True
    assert is_even(0) is True
    assert is_even(5) is False
    assert is_even(7) is False
    assert is_even(-2) is True
    assert is_even(-3) is False

"""
📝 Завдання 3. Розворот рядка 
Функція reverse_string(s) повинна повертати рядок у зворотному порядку. 
Перевір: звичайний рядок, порожній рядок, рядок з одним символом.
"""
def test_reverse_string(s):
    # TODO: додай тести для функції reverse_string
    return s[::-1]

def test_reverse_string():
    assert reverse_string("Yevhen") == "nehveY"
    assert reverse_string("") == ""
    assert reverse_string("x") == "x"

"""
📝 Завдання 4. Мінімум у списку 
Функція find_min(nums) повертає найменший елемент списку. 
Протестуй для: звичайного списку, списку з одним елементом, списку з від’ємними числами.
"""
def test_find_min(nums):
    # TODO: додай тести для функції find_min
    return min(nums)

def test_find_min():
    assert test_find_min([5, 3, 1, 2, 4]) == 1
    assert test_find_min([3]) == 3
    assert test_find_min([-5, -3, -1, -2, -4]) == -5

"""
📝 Завдання 5. Перевірка підрядка 
Функція contains_substring(s, sub) повертає True, якщо sub є в s. 
Протестуй випадки: підрядок є, підрядка нема, порожній підрядок.
"""
def test_contains_substring(s, sub):
    # TODO: додай тести для функції contains_substring
    return sub in s
    
def test_contains_substring():
    assert test_contains_substring ("Hello Yevhen", "Yevhen") is True
    assert test_contains_substring ("Hello Yevhen", "Goodbye") is False
    assert test_contains_substring ("Hello Yevhen", "") is True

"""
📝 Завдання 6. Факторіал 
Функція factorial(n) обчислює факторіал числа n. 
Протестуй: factorial(0), factorial(1), factorial(5).
"""
def test_factorial(n):
    # TODO: додай тести для функції factorial
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120

"""
📝 Завдання 7. Ділення з винятком 
Функція divide(a, b) ділить a на b. 
Перевір: звичайне ділення, ділення на від’ємне число, ділення на нуль (очікуваний ZeroDivisionError).
"""
import pytest

def test_divide(a, b):
    # TODO: додай тести для функції divide
    return a / b

assert divide(4, 2) == 2
assert divide(4, -2) == -2
with pytest.raises(ZeroDivisionError):
    divide(4, 0)

"""
📝 Завдання 8. Паліндром 
Функція is_palindrome(s) перевіряє, чи є рядок паліндромом. 
Протестуй: паліндром, непаліндром, порожній рядок.
"""
def test_is_palindrome(s):
    # TODO: додай тести для функції is_palindrome
    return s == s[::-1]

assert is_palindrome("radar") is True
assert is_palindrome("yevhen") is False
assert is_palindrome("") is True


"""
📝 Завдання 9. Сума елементів списку 
Функція sum_list(nums) повертає суму всіх чисел у списку. 
Протестуй: звичайний список, порожній список, список з від’ємними числами.
"""
def test_sum_list(nums):
    # TODO: додай тести для функції sum_list
    return sum(nums)

assert sum_list([1, 2, 3]) == 6
assert sum_list([]) == 0
assert sum_list([-1, -2, -3]) == -6

"""
📝 Завдання 10. Конвертація в верхній регістр 
Функція to_upper(s) повертає рядок у верхньому регістрі. 
Протестуй: звичайний рядок, вже великими літерами, порожній рядок.
"""
def test_to_upper(s):
    # TODO: додай тести для функції to_upper
    return s.upper()

assert to_upper("hello yevhen") == "HELLO YEVHEN"
assert to_upper("HELLO YEVHEN") == "HELLO YEVHEN"
assert to_upper("") == ""