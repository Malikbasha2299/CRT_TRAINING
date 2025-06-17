def Binary_search(key):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == key:
            break
        if key < array[mid]:
            left = mid+1
        if key > array[mid]:
            right = mid-1
    if array[mid] == key:
        print("element found at position",mid+1)
    else:
        print("element not found")
array = list(map(int , input("enter the list :").split()))
key_list = list(map(int , input("enter the keys :").split()))
for index in range(len(key_list)):
    Binary_search(key_list[index])
    