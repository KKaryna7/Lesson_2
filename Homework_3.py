# task_1
try:
    print("1. First day of the week\n2. Second day of the week\n" \
          + "3. Third day of the week\n4. Fourth day of the week\n" \
          + "5. Fifth day of the week\n6. Sixth day of the ween\n" \
          + "7. Seventh day of the week")
    user_select = int(input("Enter menu number: "))

    match user_select:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Incorrect menu item!")

except Exception as e:
    print(f"Error: {e}")

# task_2
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num1 == num2:
        print("Numbers are equal!")
    elif num1 > num2:
        print(num2, num1)
    elif num1 < num2:
        print(num1, num2)
    else:
        print("Incorrect numbers!")

except ValueError as error:
    print("Enter only integer numbers please!")
    print(f"ValueError: {error}")
except Exception as e:
    print(f"Error: {e}")

    # task_3
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        print("Choose an action:\n1. +\n2. -\n3. *\n4. /")
        user_select = int(input("Enter menu number: "))

        match user_select:
            case 1:
                result = num1 + num2
                print(f"Result: {result}")
            case 2:
                result = num1 - num2
                print(f"Result: {result}")
            case 3:
                result = num1 * num2
                print(f"Result: {result}")
            case 4:
                result = num1 / num2
                print(f"Result: {result}")

    except ZeroDivisionError as error:
        print(f"ZeroDivisionError occurred: {error}")
    except ValueError as error:
        print("Enter only integer numbers please!")
        print(f"ValueError: {error}")
    except Exception as error:
        print(f"Exception occurred: {error}")
    finally:
        print("End of calculation")
try:
    print("1. First day of the week\n2. Second day of the week\n" \
          + "3. Third day of the week\n4. Fourth day of the week\n" \
          + "5. Fifth day of the week\n6. Sixth day of the ween\n" \
          + "7. Seventh day of the week")
    user_select = int(input("Enter menu number: "))

    match user_select:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Incorrect menu item!")

except Exception as e:
    print(f"Error: {e}")

# task_2
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num1 == num2:
        print("Numbers are equal!")
    elif num1 > num2:
        print(num2, num1)
    elif num1 < num2:
        print(num1, num2)
    else:
        print("Incorrect numbers!")

except ValueError as error:
    print("Enter only integer numbers please!")
    print(f"ValueError: {error}")
except Exception as e:
    print(f"Error: {e}")