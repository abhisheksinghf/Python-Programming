class Employee:
    company = "Google"                               

harry = Employee()
abhi = Employee()
harry.salary = 300
abhi.salary = 400
print(harry.company) 
print(abhi.company) 
Employee.company = "YouTube"
print(harry.company) 
print(abhi.company)
print(harry.salary)
print(abhi.salary)                                