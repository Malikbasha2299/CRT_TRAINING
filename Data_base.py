data_base = {}
data_number = int(input("enter the no of data :"))
for i in range(data_number):
    key = input("name :")
    value = int(input("phone number :"))
    data_base [key] = value
person = input("search contact :")
if person in data_base:
    print(data_base[person])
else:
    print("contct not found")
    
    
    