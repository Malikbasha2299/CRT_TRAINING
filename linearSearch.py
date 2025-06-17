array = list(map(int , input().split()))
key = int(input("enter key :"))
for index in range(len(array)):
    if key == array[index]:
        print("key found at " , index)
        break
if key == array[index]:
    print("key found at " , index+1)
else:
    print("key is not found")