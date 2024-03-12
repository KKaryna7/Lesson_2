import re

#####
homephone_number = ['2365456', '234234', '7895784']

for val in homephone_number:
    if re.match(r'[0-9]{7}', val) and len(val) == 7:
        print("Yes")
    else:
        print("No")

home_phone = re.findall(r'\d{7}', "2365456, 234234, 6895784")
print(home_phone)

#####
mobile_phone = re.findall(r'\d', "+380(93)-456-78-95, +380(99)-435-44-76, +380(66)-567-43-67")
print(mobile_phone)

mobile_phone = re.findall(r'\+', "+380(93)-456-78-95, +380(99)-435-44-76, +380(66)-567-43-67")
print(mobile_phone)

mobile_phone = re.findall(r'\+\d{3}', "+380(93)-456-78-95, +380(99)-435-44-76, +380(66)-567-43-67")
print(mobile_phone)

mobile_phone = re.findall(r'\(\d{2}\)', "+380(93)-456-78-95, +380(99)-435-44-76, +380(66)-567-43-67")
print(mobile_phone)

mobile_phone = re.findall(r'\+\d{3}\(\d{2}\)-\d{3}-\d{2}-\d{2}', "+380(93)-456-78-95, +380(99)-435-44-76, +380(66)-567-43-67")
print(mobile_phone)

mobile_phone = re.findall(r'\d{3}-\d{2}-\d{2}', "+380(93)-456-78-95, +380(99)-435-44-76, +380(66)-567-43-67")
print(mobile_phone)

mobile_phone = ['+380(93)-456-78-95', '+380(99)-435-44-76', '+380(66)-567-43-67']

for val in mobile_phone:
    if re.match(r'\+\d{3}', val):
        print("Yes")
    else:
        print("No")

for val in mobile_phone:
    if re.findall(r'\d', val) and len(val) == 18:
        print("Yes")
    else:
        print("No")

#####
mail = ["test111@gmail.com", "homework@qqq.ua", "class@www.com"]

for val in mail:
    if re.findall(r'@', val):
        print("Yes")
    else:
        print("No")

for val in mail:
    if re.findall(r'@\w+.\w+', val):
        print("Yes")
    else:
        print("No")

for val in mail:
    if re.findall(r'\w', val) and 10 < len(val) < 15:
        print("Yes")
    else:
        print("No")

#####
people = ["Петренко Василь Іванович", "Охріменко Олександр Васльович", "Шевченко Яна Ігорівна"]

min_len = 2
max_len = 20

for val in people:
    if re.findall(r'\w+\s\w+\s\w+', val) and min_len < len(val) < max_len:
        print("Yes")
    else:
        print("No")

for val in people:
    if re.findall(r'\w+\s\w+\s\w+', val):
        print("Yes")
    else:
        print("No")


people = re.findall(r'\w+\s\w+\s\w+', "Петренко Василь Іванович, Охріменко Олександр Васльович, Шевченко Яна Ігорівна")
print(people)

people = re.findall(r'\w+', "Петренко Василь Іванович, Охріменко Олександр Васльович, Шевченко Яна Ігорівна")
print(people)
