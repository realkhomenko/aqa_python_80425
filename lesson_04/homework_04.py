adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

replacement_one = adwentures_of_tom_sawer.replace("\n", " ")
print(replacement_one)

# task 02 ==
""" Замініть .... на пробіл
"""
replacement_two = replacement_one.replace("....", " ")
print(replacement_two)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
replacement_three = replacement_two.replace("  ", " ")
print(replacement_three)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
counting = adwentures_of_tom_sawer.count('h')
print(f"Кількість символів h в рядку: {counting}")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
list_adwentures = adwentures_of_tom_sawer.split()
capital_letter_counter = sum(1 for i in list_adwentures if i and i[0].isupper())
print(capital_letter_counter)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
split_string = adwentures_of_tom_sawer.split()
i = split_string.index('Tom', 85)
print(f'Позиція, на якій слово Tom зустрічається вдруге: {i}')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('\n')
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('\n')
lowercase_letters = adwentures_of_tom_sawer_sentences[3].lower()
print(adwentures_of_tom_sawer_sentences[3])
print(lowercase_letters)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
big_letter = adwentures_of_tom_sawer.split('\n')
for letter in big_letter:
    if "By the time" in letter:
        print(f'Match: {letter}')
else:
    print('No match')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
new_list = adwentures_of_tom_sawer.split('\n')
last_sentence = new_list[-1]
words = last_sentence.split()
words_count = len(words)
print(f'Кількість слів останнього речення: {words_count}')