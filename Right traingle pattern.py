number =int(input("Enter the name :"))
num  = 1
for i in range(0, number):
    num = 1
    for j in range(1, i+1,1):
        print(num,end =" ")
        num = num+1
    print(" ")
        