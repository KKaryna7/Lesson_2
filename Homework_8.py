# task_1
def number_pow(number, power):
    if power <= 1:
        return number


    return number * number_pow(number, power - 1)


print(number_pow(4,5))

# number_pow(4, 5) -> 4 * number_pow(4, 4) => 1024
# number_pow(4, 4) -> 4 * number_pow(4, 3) => 256
# number_pow(4, 3) -> 4 * number_pow(4, 2) => 64
# number_pow(4, 2) -> 4 * number_pow(4, 1) => 16
# number_pow(4, 1) => 4

#  task_2
def stars(star, num: int):
    if num <= 0:
        return

    print(star, end="")
    stars(star, num - 1)

try:
    count = int(input("Enter number of stars: "))
    stars("*", count)
except Exception as error:
    print(error)

# stars("*", 4) -> stars(star, 3)
# stars(star, 3) -> stars(star, 2)
# stars(star, 2) -> stars(star, 1)
# stars(star, 1) -> stars(star, 0) => return

#  task_3
def summ_numbers(num1: int, num2: int) -> int:
    if num1 > num2:
        return 0

    return num1 + summ_numbers(num1 + 1, num2)


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print(f"Result: {summ_numbers(number1, number2)}")

# summ_numbers(2, 4) -> 2 + summ_numbers(3, 4) => 9
# summ_numbers(3, 4) -> 3 + summ_numbers(4, 4) => 7
# summ_numbers(4, 4) -> 4 + summ_numbers(5, 4) => 4
# summ_numbers(5, 4) -> return => 0

