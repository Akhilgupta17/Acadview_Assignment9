class Temprature:
    def Cf(self):
        far=int(input("Enter fahrenheit:"))
        x=((far-32)*(5/9))
        print("Celsius Is:",x)
    def Fc(self):
        calsius=int(input("Enter Calsius:"))
        y=((calsius*9/5)+32)
        print('fahrenheit Is:',y)
q=Temprature()
q.Cf()
q.Fc()
