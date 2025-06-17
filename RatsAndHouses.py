houses = list(map(int , input().split()))
persons = int(input("Enter the number of persons :"))
kgs = int(input("enter number of kgs :"))
target = persons * kgs
bag_weight = 0
house_count = 0
for i in range(len(houses)):
    bag_weight = bag_weight + houses[i]
    house_count = house_count + 1
    if bag_weight>=target:
        print("quantity of food = ",bag_weight)
        print("number of houses = ",house_count)
        break