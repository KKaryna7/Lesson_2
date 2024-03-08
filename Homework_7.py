# task_1
def multi_numbers(numbers: list[int]):
    n = 1
    for i in numbers:
        n *= i
    return n


try:
    nums = [1, 2, 3]
    print(multi_numbers(nums))
except ZeroDivisionError:
    print("Do not divide by zero please!")
except Exception as error:
    print(error)

# task_2
def min_number(numbers: list[int]):
    minimum = min(numbers)
    return minimum


nums = [5, 3, 1, 7, 9]
print(f"Minimum number: {min_number(nums)}")

# task_3
def simple_count(numbers: list[int]):
    count = 0
    # list_numbers = 1, 4, 11, 5, 6, 8, 13
    for number in numbers:
        is_simple = True

        if number < 2:
            continue

        for i in range(2, number):
            if number % i == 0:
                is_simple = False
                break

        if is_simple:
            count += 1
    print(f"The numbers of simple in the list: {count}")


list_numbers = [1, 4, 11, 5, 6, 8, 13, 17]
simple_count(list_numbers)

# task_4
def del_number(list_numbers: list[int], num: int):
    count = 0
    for i in list_numbers:
        if i == num:
            list_numbers.remove(i)
            count += 1
    return count


nums = [1, 5, 3, 4, 3, 2, 6, 3]
num = 5
print(f"Result: {del_number(nums, num)}")

# task_5
def two_list(nums1: list[int], nums2: list[int]):
    numbers = nums1 + nums2
    return numbers

numbers_list1 = [1, 3, 5]
numbers_list2 = [2, 4, 6]
print(f"Result: {two_list(numbers_list1, numbers_list2)}")

#  task_6
def pow_nums(numbers: list[int], power: int):
    result = []
    for i in numbers:
        result.append(i**power)
    return result


nums = [1, 2, 3, 4, 5]
pow = 2
print(f"Result: {pow_nums(nums, pow)}")
