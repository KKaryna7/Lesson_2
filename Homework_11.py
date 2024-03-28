# 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу
# всі слова, що складаються не менше ніж з семи літер.
# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.
# 3. Створіть програму, яка перевіряє текст на неприпустимі слова.
# Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.
# За підсумками роботи програми необхідно показати статистику дій.

import os
import sys
import re


TEXT_FILE = "homework.txt"
FINAL_FILE = "finish_homework.txt"

with open(TEXT_FILE, "w", encoding="utf-8") as file:
    file.write("To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To die, to sleep")

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    initial_text = file.read()
    words = initial_text.split()
    result = [word for word in words if len(word) > 7]
    print(result)

with open(FINAL_FILE, "w", encoding="utf-8") as file_result:
    file_result.write(" ".join(result))

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    initial_text = file.read()
    words = initial_text.split()
    result = len(words)
    print(f"Count words: {result}")

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    initial_text = file.read()
    restricted_word = "sleep"
    print(initial_text.count(restricted_word))
    new_text = initial_text.replace(restricted_word, "*" * len(restricted_word))
    print(new_text)

with open(FINAL_FILE, "w", encoding="utf-8") as file_result:
    file_result.write("".join(new_text))