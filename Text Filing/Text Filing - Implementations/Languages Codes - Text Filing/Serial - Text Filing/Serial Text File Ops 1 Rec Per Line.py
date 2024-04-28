"""
Code for simple serial or chorological text file operation 
like add, delete, search, update records in a text file 
using python.

This text file is for storing the records of students in a school.
Where each record contains the following information:
    1. Name : String
    2. Roll Number : Integer
    3. Class : String
    4. Marks : Real Number
Each record is stored in a single line in the text file and 
the fields are separated by a comma (,).
Name of file is student.txt
"""
def add_record():
    """
    This function adds a record to the text file.
    """
    # Open the text file in append mode
    with open('student.txt', 'at') as file:
        # Get the details of the student
        name = input('Enter the name of the student: ')
        roll_number = int(input('Enter the roll number of the student: '))
        student_class = input('Enter the class of the student: ')
        marks = float(input('Enter the marks of the student: '))

        # Write the details to the text file
        file.write(name + ',' + str(roll_number) + ',' + student_class + ',' + str(marks) + '\n')
        # Alternatively, we can use the following syntax
        # file.write(f"{name},{roll_number},{student_class},{marks}\n")
    # Close the file
    file.close()

def delete_record():
    """
    This function deletes a record from the text file.
    if the file does not exits then sytem will generate an error.
    to generate error system will use try and except block.
    """
    
    try:
        # Open the text file in read mode
        with open('student.txt', 'rt') as file:
            # Read all the lines from the text file into a list
            lines = file.readlines()

        # Close the file
        file.close()

        # Get the roll number of the student to be deleted
        roll_number = int(input('Enter the roll number of the student to be deleted: '))

        # use flag to check if the record is found or not
        flag = False

        # Delete the record from the text file
        for line in lines:
            if line.split(',')[1] == str(roll_number):
                flag = True
                lines.remove(line) # remove the line from the list
                print('Record deleted!')
                break

        # Open the text file in write mode to 
        # delete all the lines from the text file
        # and rewrite all the lines from the list
        with open('student.txt', 'wt') as file:
            # Write all the lines to the text file
            file.writelines(lines)

        # Close the file
        file.close()

        if not flag:
            print('Record not found!')

    except FileNotFoundError:
        print('File not found!')


def search_record():
    """
    This function searches for a record in the text file.
    We will use flag to check if the record is found or not.
    We will use try and except block to generate error when file not found.
    """
    try:
        # Open the text file in read mode
        with open('student.txt', 'r') as file:
            # Read all the lines from the text file
            lines = file.readlines()

        # Close the file
        file.close()

        # Get the roll number of the student to be searched
        roll_number = int(input('Enter the roll number of the student to be searched: '))

        # Search the record in the text file
        flag = False
        for line in lines:
            if line.split(',')[1] == str(roll_number):
                thisRec = line.split(',')
                print('Record found!')
                print('Name: ' + thisRec[0])
                print('Roll Number: ' + thisRec[1])
                print('Class: ' + thisRec[2])
                print('Marks: ' + thisRec[3])
                flag = True
                break

        if not flag:
            print('Record not found!')

    except FileNotFoundError:
        print('File not found!')
 

# Display all recods in the text file
def display_records():
    """
    This function displays all the records in the text file.
    We will use try and except block to generate error when file not found.
    """
    try:
        # Open the text file in read mode
        with open('student.txt', 'rt') as file:
            # Read all the lines from the text file
            lines = file.readlines()

        # Close the file
        file.close()

        # Display all the records
        for line in lines:
            print('Name: ' + line.split(',')[0])
            print('Roll Number: ' + line.split(',')[1])
            print('Class: ' + line.split(',')[2])
            print('Marks: ' + line.split(',')[3])

    except FileNotFoundError:
        print('File not found!')

def update_record():
    """
    This function updates a record in the text file.
    We will use try and except block to generate error 
    when file not found.
    """
    try:
        # Open the text file in read mode
        with open('student.txt', 'rt') as file:
            # Read all the lines from the text file into a list
            lines = file.readlines()

        # Close the file
        file.close()

        # Get the roll number of the student to be updated
        roll_number = int(input('Enter the roll number of the student to be updated: '))

        # use flag to check if the record is found or not
        flag = False

        # Update the record in the text file
        for line in lines:
            if line.split(',')[1] == str(roll_number):
                flag = True
                lines.remove(line) # remove the line from the list
                print('Record found!')
                print('Enter the new details of the student: ')
                name = input('Enter the name of the student: ')
                student_class = input('Enter the class of the student: ')
                marks = float(input('Enter the marks of the student: '))
                lines.append(name + ',' + str(roll_number) + ',' + student_class + ',' + str(marks) + '\n')
                print('Record updated!')
                break

        # Open the text file in write mode to 
        # delete all the lines from the text file
        # and rewrite all the lines from the list
        with open('student.txt', 'wt') as file:
            # Write all the lines to the text file
            file.writelines(lines)

        # Close the file
        file.close()

        if not flag:
            print('Record not found!')

    except FileNotFoundError:
        print('File not found!')

# main program showing menu and running the code functions
option = 0
while option != 6:
    print('1. Add Record')
    print('2. Delete Record')
    print('3. Search Record')
    print('4. Display Records')
    print('5. Update Record')
    print('6. Exit')
    option = int(input('Enter your option: '))
    if option == 1:
        add_record()
    elif option == 2:
        delete_record()
    elif option == 3:
        search_record()
    elif option == 4:
        display_records()
    elif option == 5:
        update_record()
    elif option == 6:
        print('Thank you!')
    else:
        print('Invalid option!')
