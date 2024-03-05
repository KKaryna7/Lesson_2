# task_1
#####
# v1
numbers = {1, 8, -4, -1, 0, 5, -4, 2, 1}
print(f"Unique numbers: {numbers}")
# v2
numbers = [1, 8, -4, -1, 0, 5, -4, 2, 1]
unique_numbers = set(numbers)
print(f"Unique numbers: {unique_numbers}")

#####
num1 = {1, 4, 2, 8, 0, 5, 9}
num2 = {3, 7, 4, 0}
print(f" First list: {num1}")
print(f"Second list: {num2}")

num3 = num1.symmetric_difference(num2)
print(f"Unique numbers in lists: {num3}")

unique_num1 = num1.intersection(num3)
count_unique_num1 = len(unique_num1)
print(f"In the first list of unique numbers: {count_unique_num1}")
unique_num2 = num2.intersection(num3)
count_unique_num2 = len(unique_num2)
print(f"In the second list of unique numbers: {count_unique_num2}")

#####
COUNT_ROW = 3
text = "Даний текст: у першому рядку записано число рядків, далі йдуть самі рядки. \
Визначте, скільки унiкальних слів міститься у цьому тексті. \
Словом вважається послідовність непробільних символів, що йдуть поспіль, слова розділені, \
одним або більшим числом пробілів або символами кінця рядка."
punctuation = ".,:"
clean_text = "".join([char for char in text if char not in punctuation])

words = clean_text.lower().split(" ")
unique_words = set(words)
count_unique_words = len(unique_words)
print(f"In the text of unique words: {count_unique_words}")

# task_2
#####
text = [("Україна", "Київ", "Одеса", "Харків"), ("Польша", "Варшава", "Вроцлав"), ("Франція", "Париж", "Ніцца")]
row1, row2, row3 = text[0], text[1], text[2]
country1, country2, country3 = text[0][0], text[1][0], text[2][0]
cities1, cities2, cities3 = text[0][1:], text[1][1:], text[2][1:]
dict_text = {country1: cities1, country2: cities2, country3: cities3}
print(dict_text)

#####
PEOPLE = 3
surname = ["Shevchenko", "Kovalenko", "Petrenko"]
name = ["Oksana", "Artem", "Maria"]

for i in range(PEOPLE):
    dict_people = {name[i]: surname[i]}
    print(dict_people)