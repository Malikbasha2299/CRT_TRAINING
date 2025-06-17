number = int(input("Enter the number :"))
duplicate = number
newnumber = number
length = 0
while number != 0:
    number = number//10
    length = length+1
while duplicate != 0:
    remainder = duplicate % 10
    sum = sum + remainder ** length
    duplicate = duplicate // 10
if sum == newnumber:
    print("amstrong")
else:
    print("not amstrong")