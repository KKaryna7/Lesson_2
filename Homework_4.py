# task_1
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


