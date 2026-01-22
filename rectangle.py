length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

if perimeter > area:
    print("Perimeter is greater than Area")
elif area > perimeter:
    print("Area is greater than Perimeter")
else:
    print("Area and Perimeter are equal")
