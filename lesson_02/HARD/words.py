# coding: UTF-8

# Задача-1
# Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
# 1. Сколько слов в тексте?
# 2. Сколько букв английского алфавита в тексте?

import  re

line = "Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту, Hello world."

line_words = line.split()
words = len(line_words)
eng_letters = re.findall(r"[a-zA-Z]", line)
eng_letters = len(eng_letters)
print("В этой строке", words, "слов.")
print("И ещё", eng_letters, "английских букв.")





