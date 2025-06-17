data_base = {}
data_number = int(input("enter the no of data :"))
for i in range(data_number):
    key = input("roolnumber :")
    value = list(map(str,input(" class branch name :").split()))
    data_base [key] = value
person = input("roolnumber :")
if person in data_base:
    print(data_base[person])
else:
    print("rool number not found")
    
    
    