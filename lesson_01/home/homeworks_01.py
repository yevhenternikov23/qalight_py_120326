# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02  == Виправте назви змінних, щоб текст виводався
helo = "Hello"
word = "world"
print(f"{helo} {word}!")

# task 03 == Зробіть так, щоб кількість бананів була
# завжди на чотири штуки більша, ніж яблук
apples = 2
banana = apples + 4

# task 04 == виправте назви змінних
Yevhen_1 = 1
Yevhen_2 = 2
Yevhen_3 = 3
Yevhen_4 = 4

# task 05 == Порахуйте периметр фігури з task 04
# та виведіть його для користувача
perimetery = Yevhen_1 + Yevhen_2 + Yevhen_3 + Yevhen_4
print(perimetery)

"""
    # Задачі 06-10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""

# task 06
"""
У Оксани було 20 марок із серії «Мистецтво» 
і 7 марок із серії «Звірі».
5 марок із серії «Мистецтво» та
1 марку із серії «Звірі» вона подарувала подружці. 
Скільки марок лишилось у Оксани?
"""
mark_art = 20
mark_animal = 7
gift_art = 5
gift_animal = 1
minus_art = mark_art - gift_art
minus_animal = mark_animal - gift_animal
total_remaining = minus_art + minus_animal
print("У Оксани залишилось:")
print("Марок із серії «Мистецтво»:", minus_art)
print("Марок із серії «Звірі»:", minus_animal)
print("Всього марок залишилось:", total_remaining)

# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple = 4
pear = apple + 5
plumb = apple - 2
total = apple + pear + plumb
print("Всього дерев посадили в саду:", total)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

temperature = 5
temperature = temperature - 10
temperature = temperature + 4
print("Температура надвечір:", temperature ,"градус")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys / 2
boys_today = boys - 1
girls_today = girls - 2
total_children = boys_today + girls_today
print("Cьогодні загалом у театральному гуртку:", int(total_children), "дітей")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book_price = 8
second_book_price = first_book_price + 2
third_book_price = (first_book_price + second_book_price) / 2
total_book_price = first_book_price + second_book_price + third_book_price
print("Перша книжка коштує:", first_book_price, "грн")
print("Друга книжка коштує:", second_book_price, "грн")
print("Третя книжка коштує:",int(third_book_price), "грн")
print("Загальна вартість усіх книг при купівлі по одному примірнику:", int(total_book_price) ,"грн")