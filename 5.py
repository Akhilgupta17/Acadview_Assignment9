class Expenditure:
    def expenditure(self):
        self.food=2000
        self.shopping=2000
        self.travel=5000
        self.total=self.food+self.shopping+self.travel
        print("total Exenditure Is:",self.total)

    def saving(self):
        self.food=500
        self.shopping=600
        self.travel=1900
        self.total1=self.food+self.shopping+self.travel
        print("total Saving Is:",self.total1)
        
    def Salary(self):
        self.salary=self.total+self.total1
        print("total Salary is :",self.salary)

q=Expenditure()
q.expenditure()
q.saving()
q.Salary()
