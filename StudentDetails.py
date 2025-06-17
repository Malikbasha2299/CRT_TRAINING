data_base = {}
for i in range(2):
    roll_no = int(input("enter roll number"))
    list = []
    name = input("enter name :")
    dept = input("enter dept :")
    year = input("enter year :")
    list.append(name)
    list.append(dept)
    list.append(year)
    data_base[roll_no] = list


Search_roll_number =int(input("Roll numbert : "))
if Search_roll_number in data_base:
    print(data_base[Search_roll_number])
else:
    print("Student details not found")
