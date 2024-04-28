"""
9618/42/M/J/23
Q3. Page 8.

A company needs a computer program to store data about its employees.
Part of the program is being written using object‑oriented programming.
The class Employee stores data about the employees. Each employee has an employee number,
a job title and hourly pay rate. The class will also store the amount they are paid each week over a
52‑week year in a 1D array.

Employee class

Attributes:
HourlyPay : REAL
stores the amount each employee gets paid each hour

EmployeeNumber : STRING
stores the employee’s unique number

JobTitle : STRING

PayYear2022 : ARRAY[0:51] OF REAL
stores the amount the employee has been paid each week

Methods:
Constructor()
initialises HourlyPay, EmployeeNumber and
JobTitle from the values passed as parameters
initialises all 52 elements in PayYear2022 to 0.0

GetEmployeeNumber()
returns the employee number

SetPay()
takes the week number and number of hours worked
that week as parameters. Calculates and stores the pay for that week in
PayYear2022. 

GetTotalPay()
returns the total of all the values in PayYear2022
"""

"""
(a) (i) Write program code to declare the class Employee.
You only need to declare the class and its constructor. Do not declare any other methods.
Use your programming language appropriate constructor.
If you are writing program code in Python, include attribute declarations using comments.
"""

class Employee:
    # HourlyPay : REAL
    # EmployeeNumber : STRING
    # JobTitle : STRING
    # PayYear2022 : ARRAY[0:51] OF REAL
    
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle):
        self.__HourlyPay = HourlyPay
        self.__EmployeeNumber = EmployeeNumber
        self.__JobTitle = JobTitle
        self.__PayYear2022 = [0.0 for i in range(52)]

    """
    (ii) The method GetEmployeeNumber() returns the employee number.
    Write program code for the method GetEmployeeNumber().
    """
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    
    """
    (iii) The method SetPay():
    • takes a week number and the number of hours worked that week as parameters
    • calculates the pay for that week by multiplying the hourly pay by the number of
    hours worked that week
    • stores the calculated pay in the appropriate index for that week in PayYear2022.
    Write program code for the method SetPay().
    """
    def SetPay(self, week, hours):
        self.__PayYear2022[week-1] = self.__HourlyPay * hours
    
    """
    (iv) The method GetTotalPay() returns the total of all the values in PayYear2022.
    Write program code for the method GetTotalPay().
    """
    def GetTotalPay(self):
        total = 0
        for i in range(52):
            total += self.__PayYear2022[i]

        #for i in self.__PayYear2022:
        #    total += i
        return total
    
    """"
    (b) The child class Manager inherits from the parent class Employee.
    A manager gets a bonus. This bonus value is a percentage, for example 10.0%.
    When calculating the pay, the number of hours the manager worked that week is increased
    by the bonus value.

    Class Manager
    Attributes:
    BonusValue : REAL stores the bonus value, 
    for example 10.0 represents a 10.0% increase
    
    Constructor()
    takes bonus value, hourly pay, employee number and job title
    as parameters
    initialises BonusValue to its parameter value
    
    SetPay()
    takes the week number and number of hours worked in that week as
    parameters
    increases the number of hours worked by the bonus value
    calls the SetPay() method from the parent class
    """

    """
    (i) Write program code to declare the class Manager.
    You only need to declare the class and its constructor. Do not declare any other methods.
    Use your programming language appropriate constructor.
    If you are writing in Python, include attribute declarations using comments.
    """

class Manager(Employee):
    # BonusValue : REAL

    def __init__(self, BonusValue, HourlyPay, EmployeeNumber, JobTitle):
        super().__init__(HourlyPay, EmployeeNumber, JobTitle)
        self.__BonusValue = BonusValue
        
    """
    (ii) Write program code for the method SetPay().
    """
    def SetPay(self, week, hours):
        hours += hours * (self.__BonusValue / 100)
        super().SetPay(week, hours)
    
    """
    (c) The main program has a global 1D array, EmployeeArray, to store data about
    eight employees. Each employee is stored as an object of type Employee.
    The file Employees.txt stores data about the employees, in the order:
        • hourly pay
        • employee number
        • bonus value (where included)
        • job title.

    Only employees who are managers have a bonus value saved. For example:
        • The first employee is a Junior Developer, with employee number 12452 and an hourly
        pay of $15.22. This employee does not have a bonus value.
        • The third employee is an Interface Manager, with employee number 02586 and an hourly
        pay of $22.50. This employee has a bonus value of 5.25%.

    Write the main program to:
    • declare the array to store data about 8 employees
    • read in the data from the file for each employee
    • instantiate each employee as either Employee (if the employee does not have a bonus
    value) or Manager (if the employee has a bonus value).
    """
"""
(d) The file HoursWeek1.txt stores the number of hours each employee has worked in week 1,
    in the order as one field per line:
        • employee number
        • number of hours worked.

    For example, the first set of data is for employee 21548 who has worked 50.0 hours.
    The procedure EnterHours():
        • reads in the values from the file
        • finds the location of each employee in EmployeeArray
        • calls the method SetPay() for each employee.
    Write program code for EnterHours().
"""

def EnterHours():
    file = open("HoursWeek1.txt", "rt")
    for i in range(8):
        employeeNumber = file.readline().strip()
        hours = float(file.readline().strip())
        for j in range(8):
            if EmployeeArray[j].GetEmployeeNumber() == employeeNumber:
                EmployeeArray[j].SetPay(0, hours)
                break
    file.close()


# main program
EmployeeArray = [None for i in range(8)]
file = open("Employees.txt", "rt")
for i in range(8):
    # data is saved one field per line
    data = file.readline().strip()
    hourlyPay = float(data)
    employeeNumber = file.readline().strip()
    x = file.readline().strip()
    temp = None
    bonusValue = 0
    jobTitle = ''
    """
    try:
        temp = float(x)
        bonusValue = temp
        jobTitle = file.readline().strip()
    except ValueError:
        jobTitle = x
    """
    if '.' in x:
        bonusValue = float(x)
        jobTitle = file.readline().strip()
    else:
        jobTitle = x

    if bonusValue == 0:
        EmployeeArray[i] = Employee(hourlyPay, employeeNumber, jobTitle)
    else:
        EmployeeArray[i] = Manager(bonusValue, hourlyPay, employeeNumber, jobTitle)
file.close()

"""
(e) (i) The main program needs to call EnterHours() and use the method GetTotalPay()
to output the employee number and total pay for each of the eight employees.
Amend the main program to perform these tasks.
"""
EnterHours()
for i in range(8):
    print(EmployeeArray[i].GetEmployeeNumber(), EmployeeArray[i].GetTotalPay())
