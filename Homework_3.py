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