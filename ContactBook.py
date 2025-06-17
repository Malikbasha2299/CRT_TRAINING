data_base = {}
data_number = int(input("Enter the no of data :"))
for i in range(data_number):
    key = input("name : ")
    value = int(input("Phone number : "))
    data_base[key] = value
person = input("Search contact : ")
if person in data_base:
    print(data_base[person])
else:
    print("contact not found")