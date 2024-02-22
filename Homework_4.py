# task_1
try:
    text = input("Enter string: ")

    letter_count = 0
    digit_count = 0

    for symbol in text:
        if symbol.isalpha():
            letter_count += 1
        elif symbol.isdigit():
            digit_count += 1

    print(f"Numbers of letter: {letter_count}")
    print(f"Numbers of digit: {digit_count}")
except Exception as e:
    print(e)

# task_2
count = 0
text = input("Enter string: ")
symbol = input("Enter symbol for search: ")

for i in text:
    if i == symbol:
        count += 1
print(f"Numbers of symbol in string: {count}")

# task_3
text = input("Enter your string: ")
word_search = input("Enter word for search: ")
word_replace = input("Enter word for replace: ")

text_replace = text.replace(word_search, word_replace, 1)
print(text_replace)

# task_4
text = "Hello World"
print(text[2])
print(text[-2])
print(text[:5])
print(text[:-2])
print(text[::2])
print(text[1::2])
print(text[::-1])
print(text[::-2])
print(len(text))


