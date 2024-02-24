# task_PLUS_1
text = "хотіли повідомити, що в середу, 07.02.2024 о 19:15 за київським часом " \
       + "відбудеться перше заняття з курсу Python Basic. ваш стандартний розклад – середа " \
       + "о 19:15 та субота о 12:00. тривалість заняття - 2 години."
# print(text)
search_symbol = ". "
symbol_index = text.find(search_symbol)
first_sentence = text[:symbol_index + 2]
sentence_ = text[symbol_index + 2:]
symbol_index2 = sentence_.find(search_symbol)
second_sentence = sentence_[:symbol_index2 + 2]
third_sentence = sentence_[symbol_index2 + 2:]
# print(first_sentence)
# print(second_sentence)
# print(third_sentence)
print(first_sentence.capitalize() + second_sentence.capitalize() + third_sentence.capitalize())

letter_count = 0
digit_count = 0

for symbol in text:
       if symbol.isalpha():
            letter_count += 1
       elif symbol.isdigit():
            digit_count += 1

print(f"Numbers of letter: {letter_count}")
print(f"Numbers of digit: {digit_count}")

symbols_punctuation1 = ","
symbols_punctuation2 = "."
symbols_punctuation3 = ":"
symbols_punctuation4 = "-"
symbols_punctuation5 = "!"

symbols1_count = 0
symbols2_count = 0
symbols3_count = 0
symbols4_count = 0
symbols5_count = 0

for i1 in text:
       if i1 == symbols_punctuation1:
              symbols1_count += 1
for i2 in text:
       if i2 == symbols_punctuation2:
              symbols2_count += 1
for i3 in text:
       if i3 == symbols_punctuation3:
              symbols3_count += 1
for i4 in text:
       if i4 == symbols_punctuation4:
              symbols4_count += 1
for i5 in text:
       if i5 == symbols_punctuation5:
              symbols5_count += 1
summ_symbols = int(symbols1_count) + int(symbols2_count) + int(symbols3_count) + int(symbols4_count) + int(symbols5_count)
print(f"Symbols punctuation: {summ_symbols}")
print(f"Numbers '!': {symbols5_count}")

# task_PLUS_2
symbol = "* "

#########
counter = 5
whitespaces = 0

for i in range(5):
       for j in range(whitespaces):
              print("  ", end="")
       for j in range(counter):
              print(symbol, end="")

       if i < 5:
              counter -= 1
              whitespaces += 1
       print()

#########
counter = 1
for i in range(5):
       for j in range(counter):
              print(symbol, end="")
       print()
       counter += 1

#########
counter = 5
whitespaces = 0

for i in range(5):
       for j in range(whitespaces):
              print("  ", end="")
       for j in range(counter):
              print(" ", symbol, end="")

       if i < 5:
              counter -= 1
              whitespaces += 1
       print()

#########
counter = 1
whitespaces = 5

for i in range(5):
       for j in range(whitespaces):
              print("  ", end="")
       for j in range(counter):
              print(" ", symbol, end="")

       if i < 5:
              counter += 1
              whitespaces -= 1
       print()

#########
counter = 5
whitespaces = 1
for i in range(5):
    for j in range(whitespaces):
        print("  ", end="")
    for j in range(counter):
        print(symbol, end="")
    for j in range(whitespaces):
        print("  ", end="")

    if i < 2:
        counter -= 2
        whitespaces += 1
    else:
        counter += 2
        whitespaces -= 1
    print()

##########
for i in range(5):
    if i == 0 or i == 4:
        print(symbol, end="")
        for j in range(3):
            print("  ", end="")
        print(symbol, end="")
    if i == 1 or i == 3:
        for j in range(2):
            print(symbol, end="")
        print("  ", end="")
        for j in range(2,4):
            print(symbol, end="")
    elif i == 2:
        for j in range(5):
            print(symbol, end="")
    print()

##########
counter = 1
for i in range(5):
    print(symbol)
    if i in range(0,3):
        print(symbol, end="")
        counter += 1
    if i == 1:
        print(symbol, end="")
        counter += 2

##########
counter = 5
whitespaces = 1
for i in range(counter):
    if i == 0 or i == 4:
        print("       ", symbol, end="")
    for j in range(whitespaces):
        if i == 1 or i == 3:
            print("     ", symbol, end="")
            print(symbol, end="")
    for j in range(whitespaces):
        if i == 2:
            print("   ", symbol*3, end="")
    print()

##########
counter = 5

for i in range(5):
       for j in range(counter):
              print(symbol, end="")

       if i < 5:
              counter -= 1
       print()

#########
counter = 1
whitespaces = 5

for i in range(5):
       for j in range(whitespaces):
              print("  ", end="")
       for j in range(counter):
              print(symbol, end="")

       if i < 5:
              counter += 1
              whitespaces -= 1
       print()

