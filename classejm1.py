# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:40:50 2019

@author: Juan Carlos
"""

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(a,name, salary):
      a.name = name
      a.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d", Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

"This would create first object of Employee class"      
emp12 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp7 = Employee("Sandra", 5000)
emp8 = Employee("Ana",8000)
emp9 = Employee("Briguitte",8000)
emp10 = Employee ('Juan',1200)
emp11 = Employee ('Carlos',1600)
emp11.displayEmployee()
emp12.displayEmployee()
emp10.displayEmployee()
emp9.displayEmployee()
emp8.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

