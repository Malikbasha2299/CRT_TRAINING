array = list(map(int , input().split()))
key = int(input("enter key :"))
left = 0
right = len(array) - 1
while left <= right:
    mid = (left + right) // 2
    if array[mid] == key:
        break
    if key > array[mid]:
        left = mid + 1
    if key < array[mid]:
        right = mid - 1
if array[mid] == key:
    print("element found at index",mid)
else:
    print("element not found")

    