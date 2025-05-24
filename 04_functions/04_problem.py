import math
def circle(r):
    area = (math.pi)*r**2
    circumference = 2*(math.pi)*r
    return area, circumference
radius = int(input("Enter the radius of the circle: "))
area, circumference = circle(radius)
print("Area of the circle is: ",area)
print("Circumference of the circle is: ",circumference)

