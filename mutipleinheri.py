#program to demonstrate multiple inheritance Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)
        
# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)
        
# Child class
class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)

# Create object of Employee
emp = Employee()
# access data
emp.person_info('Shrutika Bagul', 18)
emp.company_info('Microsoft', 'India')
emp.Employee_info(120000, 'Python')
