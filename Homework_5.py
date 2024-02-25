# task_1
import random

NUMS_SIZE = 10
numbers = []

for i in range(NUMS_SIZE):
    numbers.append(random.randint(-5, 5))
print(f"List: {numbers}")

#####
negative_numbers = 0

for number in numbers:
    if number < 0:
        negative_numbers += number
print(f"Sum of negative numbers: {negative_numbers}")

#####
even_numbers = 0

for number in numbers:
    if number % 2 == 0:
        even_numbers += number
print(f"Sum of even numbers: {even_numbers}")

#####
odd_numbers = 0

for number in  numbers:
    if number % 2 != 0:
        odd_numbers += number
print(f"Sum of odd numbers: {odd_numbers}")

#####
multi_numbers_3 = 1

for number in numbers:
    if number % 3 == 0:
        multi_numbers_3 *= number
print(f"The product of numbers in multiples of 3: {multi_numbers_3}")

#####
index_min_numbers = numbers.index(min(numbers))
index_max_numbers = numbers.index(max(numbers))

print(f"Minimum number index: {index_min_numbers}")
print(f"Maximum number index: {index_max_numbers}")

if index_min_numbers > index_max_numbers:
    index_min_numbers, index_max_numbers = index_max_numbers, index_min_numbers

multi_numbers = 1
for number in range(index_min_numbers + 1 , index_max_numbers):
    multi_numbers *= numbers[number]
print(f"Product of numbers between minimum and maximum: {multi_numbers}")

#####
number1 = 0
number2 = 0

for i in range(NUMS_SIZE):
    if numbers[i] > 0:
        number1 = i
        break
for i in range(NUMS_SIZE - 1, - 1, - 1):
    if numbers[i] > 0:
        number2 = i
        break
print(f"First and last positive numbers: {number1, number2}")

summ_numbers = 0
for i in range(number1 + 1, number2):
    summ_numbers += numbers[i]
print(f"The sum of the numbers between the first and the last positive numbers: {summ_numbers}")

# task_2
numbers = [-4, 7, 2, 6, 9, -3, 0, 5, 1]
print(f"List: {numbers}")

even_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
print(f"Even numbers: {even_numbers}")

odd_numbers = []
for i in numbers:
    if i % 2 != 0:
        odd_numbers.append(i)
print(f"Odd numbers: {odd_numbers}")

negative_numbers = []
positive_numbers = []
for i in numbers:
    if i < 0:
        negative_numbers.append(i)
    if i > 0:
        positive_numbers.append(i)
print(f"Negative numbers: {negative_numbers}")
print(f"Positive numbers: {positive_numbers}")
