"""
9608/42/PRE/M/J/18
*Task2 is make a python code for the following pre release material*

A toy shop needs a computer system to store information about its toys.
The developer writes a program using object-oriented programming.
• A toy has the properties:
Name (for example, Train engine)
ID (for example, TE11)
Price (for example, 0.99)
Minimum age (for example, 4)
• A computer game is a type of toy; it has the properties of toy, and:
Category (for example, Car racing)
Console (for example, Camstation)
• A vehicle is a type of toy; it has the properties of toy, and:
Type (for example, Car)
Height (for example, 4)
Length (for example, 15)
Weight (for example, 0.2)

Write program code to create the Toy class. Make sure:
• the properties are declared as private
• you have a constructor
• you have get and set methods for each property.
"""
class Toy:
    # Attribute declarations as comments
    # declare name as string
    # declare ID as string
    # declare price as float
    # declare min_age as integer

    def __init__(self, name, ID, price, min_age):
        self.__name = name
        self.__ID = ID
        self.__price = price
        self.__min_age = min_age

    # getters
    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__ID

    def get_price(self):
        return self.__price

    def get_min_age(self):
        return self.__min_age

    # setters
    def set_name(self, name):
        self.__name = name

    def set_ID(self, ID):
        self.__ID = ID

    def set_price(self, price):
        self.__price = price

    def set_min_age(self, min_age):
        self.__min_age = min_age

"""
Write program code to create the ComputerGame and Vehicle classes. Make sure:
• the properties are declared as private
• you have a constructor
• you have get and set methods for each property
• the classes inherit the properties from the Toy class.
"""
class ComputerGame(Toy):
    # Attribute declarations as comments
    # declare category as string
    # declare console as string

    def __init__(self, name, ID, price, min_age, category, console):
        super().__init__(name, ID, price, min_age)
        self.__category = category
        self.__console = console

    # getters
    def get_category(self):
        return self.__category

    def get_console(self):
        return self.__console

    # setters
    def set_category(self, category):
        self.__category = category

    def set_console(self, console):
        self.__console = console

class Vehicle(Toy):
    # Attribute declarations as comments
    # declare type as string
    # declare height as float
    # declare length as float
    # declare weight as float

    def __init__(self, name, ID, price, min_age, type, height, length, weight):
        super().__init__(name, ID, price, min_age)
        self.__type = type
        self.__height = height
        self.__length = length
        self.__weight = weight

    # getters
    def get_type(self):
        return self.__type

    def get_height(self):
        return self.__height

    def get_length(self):
        return self.__length

    def get_weight(self):
        return self.__weight

    # setters
    def set_type(self, type):
        self.__type = type

    def set_height(self, height):
        self.__height = height

    def set_length(self, length):
        self.__length = length

    def set_weight(self, weight):
        self.__weight = weight

"""
Create 5 instances of ComputerGame and Vehicle with appropriate example data, 
in the main program. Store the objects in arrays CG_array and Veh_arr. 
The data for one instance of Vehicle is given to get you started as an example.

Name = "Red Sports Car"
ID = "RSC13"
Price = 15.00
Minimum age = 6
Type = "Car"
Height = 3.3
Length = 12.1
Weight = 0.08
"""
CG_array = []
Veh_arr = []
# instance 1 of ComputerGame
CG_array.append(ComputerGame("Car racing", "CG1", 15.00, 6, "Red Sports Car", "RSC13"))

# instance 2 of ComputerGame
CG_array.append(ComputerGame("Shooting 1", "CG2", 10.00, 9, "Fortnite", "VEH13"))

# instance 3 of ComputerGame
CG_array.append(ComputerGame("Shooting 2", "CG3", 13.00, 9, "Call of Duty", "VEH13"))

# instance 4 of ComputerGame
CG_array.append(ComputerGame("Shooting 3", "CG4", 5.00, 9, "Battlefield", "VEH13"))

# instance 5 of ComputerGame
CG_array.append(ComputerGame("Shooting 4", "CG5", 20.00, 9, "PUBG", "VEH13"))

# instance 1 of Vehicle
Veh_arr.append(Vehicle("Red Sports Car", "RSC13", 15.00, 6, "Car", 3.3, 12.1, 0.08))

# instance 2 of Vehicle
Veh_arr.append(Vehicle("Blue Sports Car", "BSC13", 15.00, 6, "Car", 3.3, 12.1, 0.08))

# instance 3 of Vehicle
Veh_arr.append(Vehicle("Green Sports Car", "GSC13", 15.00, 6, "Car", 3.3, 12.1, 0.08))

# instance 4 of Vehicle
Veh_arr.append(Vehicle("Yellow Sports Car", "YSC13", 15.00, 6, "Car", 3.3, 12.1, 0.08))

# instance 5 of Vehicle
Veh_arr.append(Vehicle("Orange Sports Car", "OSC13", 15.00, 6, "Car", 3.3, 12.1, 0.08))

"""
A procedure searchID prompts the user to input the ID for a toy. The program finds that toy and outputs the
values of its properties in an appropriate format.
Write the procedure and test it with appropriate data.
"""

def searchID():
    ID = input("Enter ID of toy: ")
    for i in CG_array:
        if i.get_ID() == ID:
            print("Name: " + i.get_name())
            print("ID: " + i.get_ID())
            print("Price: " + str(i.get_price()))
            print("Minimum age: " + str(i.get_min_age()))
            print("Category: " + i.get_category())
            print("Console: " + i.get_console())
            print()
    
    for i in range(len(Veh_arr)):
        if Veh_arr[i].get_ID() == ID:
            print("Name: " + Veh_arr[i].get_name())
            print("ID: " + Veh_arr[i].get_ID())
            print("Price: " + str(Veh_arr[i].get_price()))
            print("Minimum age: " + str(Veh_arr[i].get_min_age()))
            print("Type: " + Veh_arr[i].get_type())
            print("Height: " + str(Veh_arr[i].get_height()))
            print("Length: " + str(Veh_arr[i].get_length()))
            print("Weight: " + str(Veh_arr[i].get_weight()))
            print()

"""
A procedure allows the user to input a number to be used as a discount rate. The price of all the toys
will be reduced by that number. For example, 10 would reduce the price of all toys by 10%.
Write the procedure and test it with appropriate data.
"""
def discount():
    discount = int(input("Enter discount rate: "))
    # discount all computer game toys by discount rate
    for i in CG_array:
        i.set_price(i.get_price() * (1 - (discount / 100)))

    # discount all vehicle toys by discount rate
    for i in Veh_arr:
        i.set_price(i.get_price() * (1 - (discount / 100)))

"""
The shop would like the program to sort the objects in the ComputerGame class in ascending order of price USING BUBBLE SORT, and output the values of their properties.

Write bubble sort algorithm to sort and output the ComputerGame array in ascending order of price.
"""
def bubbleSort():
    # bubble sort algorithm
    for i in range(len(CG_array)):
        for j in range(len(CG_array) - 1):
            if CG_array[j].get_price() > CG_array[j + 1].get_price():
                CG_array[j], CG_array[j + 1] = CG_array[j + 1], CG_array[j]

    # output values of properties
    print("Sorted by price using bubble sort: ")
    for i in CG_array:
        print("Name: " + i.get_name())
        print("ID: " + i.get_ID())
        print("Price: " + str(i.get_price()))
        print("Minimum age: " + str(i.get_min_age()))
        print("Category: " + i.get_category())
        print("Console: " + i.get_console())
        print()

# write insertion sort algorithm to sort and output the ComputerGame array in ascending order of price.
def insertionSort():
    # insertion sort algorithm
    for i in range(1, len(CG_array)):
        key = CG_array[i]
        j = i - 1
        while j >= 0 and key.get_price() < CG_array[j].get_price():
            CG_array[j + 1] = CG_array[j]
            j -= 1
        CG_array[j + 1] = key

    # output values of properties
    print("Sorted by price using insertion sort: ")
    for i in CG_array:
        print("Name: " + i.get_name())
        print("ID: " + i.get_ID())
        print("Price: " + str(i.get_price()))
        print("Minimum age: " + str(i.get_min_age()))
        print("Category: " + i.get_category())
        print("Console: " + i.get_console())
        print()

# test searchID procedure
searchID()

# test discount procedure
discount()

# test bubbleSort procedure
bubbleSort()

# test insertionSort procedure
insertionSort()

# end of program