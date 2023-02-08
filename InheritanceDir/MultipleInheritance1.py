9# Multiple Inheritance
class A:
    def EmpDetails(self):
        self.name = input("Enter Employee Name : ")
        self.age = int(input("Enter Employee Age : "))
class B:
    def EmpSalary(self):
        self.sal = int(input("Enter Employee Salary : "))
class C(A,B):
    def Empdisplay(self):
        print("EMPLOYEE DETAILS")
        print("*******************")
        print("Name\tAge\t\tSalary ")
        print(self.name,"\t",self.age,"\t",self.sal)
objC = C()
objC.EmpDetails()
objC.EmpSalary()
objC.Empdisplay()