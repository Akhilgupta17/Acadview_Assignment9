class circle:
    def area(self):
        r=int(input("Enter Radius:"))
        x=(3.14*(r**2))
        print("Area Is:",x)
    def circumference(self):
        r=int(input("Enter Radius:"))
        y=(2*3.14*r)
        print("Circumference Is:",y)

        
q=circle()
q.area()
q.circumference()
