rows = int(input("Enter of rows :"))
cols = (rows * 2)- 1
spaces = rows - 1
for row in range(1, rows + 1 ):
    for space in range(1, spaces + 1):
        print(" ",end = "")
    for star in range(1, row +1):
        print("*" , end = " ")
    spaces = spaces - 1
    print()
spaces = 1
rows = rows - 1
stars = rows
for row in range(1, rows +1):
    for space in range(1, spaces +1):
        print(" ",end= "")
    for star in range(1, stars + 1):
        print("*",end=" ")
    spaces = spaces + 1
    stars = stars - 1
    print()
    
