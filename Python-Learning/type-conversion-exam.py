#circle computations

pi=3.14
radius=input('r:')     #radius is String, must be type conversion
radius=float(radius)


area=pi*(radius**2)

round=2*pi*radius

print("Area of Circle: " + str(area) + " Round of Circle:" + str(round))
