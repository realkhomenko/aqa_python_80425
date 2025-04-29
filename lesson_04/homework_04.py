adventures_of_tom_sawyer = """\
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

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawyer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("\n", " ")
print(adventures_of_tom_sawyer)

# task 02 ==
""" Замініть .... на пробіл
"""
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("....", " ")
print(adventures_of_tom_sawyer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adventures_of_tom_sawyer = " ".join(adventures_of_tom_sawyer.split())
print(adventures_of_tom_sawyer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
adventures_of_tom_sawyer_count = adventures_of_tom_sawyer.count('h')
print(f'Кількість літер h у тексті: {adventures_of_tom_sawyer_count}')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
adventures_of_tom_sawyer_list = adventures_of_tom_sawyer.split()
capital_letter_counter = sum(1 for i in adventures_of_tom_sawyer_list if i and i[0].isupper())
print(f'Кількість слів у тексті з великої літери: {capital_letter_counter}')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
adventures_of_tom_sawyer_index = adventures_of_tom_sawyer.find("Tom", adventures_of_tom_sawyer.find("Tom") + 1)
print(f'Позиція на якій слово Tom зустрічається вдруге: {adventures_of_tom_sawyer_index}')

# task 07
""" Розділіть змінну adventures_of_tom_sawyer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawyer_sentences
"""
adventures_of_tom_sawyer_sentences = adventures_of_tom_sawyer.split(".")

# task 08
""" Виведіть четверте речення з adventures_of_tom_sawyer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(f'4-те реченя з adventures_of_tom_sawyer_sentences: {(adventures_of_tom_sawyer_sentences[4])}')
adventures_of_tom_sawyer_sentences_lower = adventures_of_tom_sawyer_sentences[4].lower()
print(f'4-те реченя з adventures_of_tom_sawyer_sentences в нижньому регістрі: {adventures_of_tom_sawyer_sentences_lower}')

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
string_entry = adventures_of_tom_sawyer.split(".")

for entry in string_entry:
    entry = entry.strip()
    if entry.startswith("By the time"):
        print(f"Речення яке починається з 'By the time': {entry}")

# task 10
""" Виведіть кількість слів останнього речення з adventures_of_tom_sawyer_sentences.
"""
adventures_of_tom_sawyer_sentences = [sentence.strip() for sentence in adventures_of_tom_sawyer_sentences if sentence.strip()]
last_sentence = adventures_of_tom_sawyer_sentences[-1]
words_in_last_sentence = last_sentence = last_sentence.split()
count_words = len(words_in_last_sentence)
print(f'Кількість слів останього реченя: {count_words}')