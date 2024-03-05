import random

matrix = []

for i in range(10):
    matrix.append([])
    for j in range(10):
        matrix[i].append(random.randint(10, 99))

# print(matrix)

for row in matrix:
    for number in row:
        print(number, end=" ")
    print()

number0 = matrix[0][0]
NUMS = 10

#####
sum_main_diagonal = 0

for i in range(NUMS):
    sum_main_diagonal += matrix[i][i]
print(f"The sum of the numbers of the main diagonal of the matrix: {sum_main_diagonal}")

#####
numbers_secondary_diagonal = []

for i in range(NUMS):
    numbers_secondary_diagonal.append(matrix[i][NUMS - i - 1])
print(f"Numbers in secondary diagonal: {numbers_secondary_diagonal}")

min_secondary = min(numbers_secondary_diagonal)
max_secondary = max(numbers_secondary_diagonal)
print(f"Minimum and maximum numbers of the secondary diagonsl: {min_secondary, max_secondary}")

#####
try:
    column = int(input("Enter the column number from 0 to 9: "))
    column_numbers = []

    for i in range(NUMS):
        column_numbers.append(matrix[i][column])
    print(f"The column numbers: {column_numbers}")

except ValueError as error:
    print("Enter only integer numbers please!")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")

try:
    row = int(input("Enter the row number from 0 to 9: "))
    row_numbers = []

    for i in range(NUMS):
        row_numbers.append(matrix[row][i])
    print(f"The row numbers: {row_numbers}")

except ValueError as error:
    print("Enter only integer numbers please!")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")

#####
try:
    column1 = int(input("Enter the column number from 0 to 9: "))
    column2 = int(input("Enter the column number from 0 to 9: "))
    column1_numbers = []
    column2_numbers = []

    for i in range(NUMS):
        column1_numbers.append(matrix[i][column1])
    print(f"The column numbers: {column1_numbers}")
    for i in range(NUMS):
        column2_numbers.append(matrix[i][column2])
    print(f"The column numbers: {column2_numbers}")

#  Думала зробити зміну стовпчиків і рядків через множинне привласнення, але не вийшло
    # for i in range(NUMS):
    column1_numbers[i][column1], column2_numbers[i][column2] = column1_numbers[i][column2], column2_numbers[i][column1]
    # print()

    for row in matrix:
        for number in row:
            print(number, end=" ")
        print()

except ValueError as error:
    print("Enter only integer numbers please!")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")

# first_col = 2
# second_col = 4
#
# if 0 < first_col <= 5 and 0 < second_col <= 5:
#     for i in range(5):
#         numbers[i][first_col - 1], numbers[i][second_col - 1] = numbers[i][second_col - 1], numbers[i][first_col - 1]
# else:
#     print("Invalid columns!")
#
# print()
# for i in range(5):
#     for j in range(5):
#         print(numbers[i][j], end=" ")
#     print()
#
# print()
# first_row = 2
# second_row = 4
#
# if 0 < first_row <= 5 and 0 < second_row <= 5:
#     numbers[first_row - 1], numbers[second_row - 1] = numbers[second_row - 1], numbers[first_row - 1]
#     # print(numbers[first_row - 1])
#     # print(numbers[second_row - 1])
# else:
#     print("Invalid rows!")
#
# for i in range(5):
#     for j in range(5):
#         print(numbers[i][j], end=" ")
#     print()
#
# print()