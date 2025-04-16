# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

#task 01
alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"\n
"That depends a good deal on where you want to get to," said the Cat.\n
"I don't much care where ——" said Alice."\n
"Then it doesn't matter which way you go," said the Cat.\n
"—— so long as I get somewhere," Alice added as an explanation.\n
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''

#task 02
quantity = alice_in_wonderland.count("'")
print("Символи одинарної лапки (') у тексті:", quantity)

#task 03
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_see_area = 436402
azov_see_area = 37800
total_area = black_see_area + azov_see_area
print("Площа яку займають разом Чорне та Азоске море:", total_area, "км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_quantity_of_goods = 375291
first_syllable = total_quantity_of_goods - 222950
second_syllable = 250449 - first_syllable
third_syllable = 222950 - second_syllable
print("Кількість товарів, що розміщені на кожному складі:", end=" ")
print("1-й склад:", first_syllable, "2-й склад:", second_syllable, "3-й склад:", third_syllable)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
number_of_month = 18
payment_in_installments = 1179
computer_cost = number_of_month * payment_in_installments
print("Вартість компьютера:",computer_cost)


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print("Остача від діленя:", end=" ")
print(a, b, c, d, e, f, sep=",")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
large_pizza = 274
medium_pizza = 218
juice = 35
pie = 350
water = 21
total_amount = large_pizza + medium_pizza + juice + pie + water
print("Загальна сума витрат:", total_amount)


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
number_of_photos = 232
photo_on_the_page = 8
page_amount = int(number_of_photos / photo_on_the_page)
print("Сторінок знадобиться:", page_amount)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
fuel_consumption = 9
fuel_tank = 48
gasoline_for_the_trip = (distance / 100) * fuel_consumption
amount_refueled = int(gasoline_for_the_trip / fuel_tank)
print(gasoline_for_the_trip)
print(amount_refueled)