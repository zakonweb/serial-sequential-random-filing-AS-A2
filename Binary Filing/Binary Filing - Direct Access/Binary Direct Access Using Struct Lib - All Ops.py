"""
Write code og binary random file to access it directly for every record.
Each record is made up of 3 fields:
Student ID (integer)
Student Name (string)
Student Fee (float)
This program will make use of the struct module to pack and unpack the data.
And present the menu interface to the user to perform the following operations:
1. Add a new record
2. Display all records
3. Search a record by ID
4. Modify a record by ID
5. Delete a record by ID
6. Exit
"""
import struct
import os
import sys

# Define the record structure
record_struct = struct.Struct('i 20s f')

# Add a new record
def add_record():
    # Get the data from the user
    student_id = int(input('Enter student ID: '))
    student_name = input('Enter student name: ')
    student_fee = float(input('Enter student fee: '))
    # Pack the data into a record
    record = record_struct.pack(student_id, student_name.encode(), student_fee)
    # Write the record to the file
    with open('students.dat', 'ab') as f:
        f.write(record)
    # Display a message to the user
    print('Record added successfully.')

    # Close the file
    f.close()

# Display all records
def display_records():
    # Open the file for reading
    with open('students.dat', 'rb') as f:
        # Read the first record
        record = f.read(record_struct.size)
        # Loop until the end of the file
        while record:
            # Unpack the record
            student_id, student_name, student_fee = record_struct.unpack(record)
            # Display the record
            print('Student ID:', student_id)
            print('Student Name:', student_name.decode().strip('\x00'))
            print('Student Fee:', student_fee)
            print()
            # Read the next record
            record = f.read(record_struct.size)
    # Close the file
    f.close()

# Search a record by ID
def search_record():
    # Get the ID to search for
    student_id = int(input('Enter student ID: '))

    # Open the file for reading
    with open('students.dat', 'rb') as f:
        # Read the first record
        record = f.read(record_struct.size)
        # Loop until the end of the file
        while record:
            # Unpack the record
            id, name, fee = record_struct.unpack(record)
            # Check if the ID matches
            if id == student_id:
                # Display the record
                print('Student ID:', id)
                print('Student Name:', name.decode().strip('\x00'))
                print('Student Fee:', fee)
                print()
                # Close the file
                f.close()
                # Return from the function
                return
            # Read the next record
            record = f.read(record_struct.size)
    # Close the file
    f.close()
    # Display a message to the user
    print('Record not found.')

# Modify a record by ID
def modify_record():
    # Get the ID to modify
    student_id = int(input('Enter student ID: '))

    # Open the file for reading and writing
    with open('students.dat', 'r+b') as f:
        # Read the first record
        record = f.read(record_struct.size)
        # Loop until the end of the file
        while record:
            # Unpack the record
            id, name, fee = record_struct.unpack(record)
            # Check if the ID matches
            if id == student_id:
                # Get the data from the user
                student_name = input('Enter student name: ')
                student_fee = float(input('Enter student fee: '))
                # Pack the data into a record
                record = record_struct.pack(student_id, student_name.encode(), student_fee)
                # Move the file pointer to the beginning of the record
                f.seek(-record_struct.size, os.SEEK_CUR)
                # Write the record to the file
                f.write(record)
                # Display a message to the user
                print('Record modified successfully.')
                # Close the file
                f.close()
                # Return from the function
                return
            # Read the next record
            record = f.read(record_struct.size)
    # Close the file
    f.close()
    # Display a message to the user
    print('Record not found.')

# Delete a record by ID
def delete_record():
    # Get the ID to delete
    student_id = int(input('Enter student ID: '))

    # Open the file for reading and writing
    with open('students.dat', 'r+b') as f:
        # Read the first record
        record = f.read(record_struct.size)
        # Loop until the end of the file
        while record:
            # Unpack the record
            id, name, fee = record_struct.unpack(record)
            # Check if the ID matches
            if id == student_id:
                # Move the file pointer to the beginning of the record
                f.seek(-record_struct.size, os.SEEK_CUR)
                # Write a blank record to the file
                f.write(record_struct.pack(0, ''.encode(), 0.0))
                # Display a message to the user
                print('Record deleted successfully.')
                # Close the file
                f.close()
                # Return from the function
                return
            # Read the next record
            record = f.read(record_struct.size)
    # Close the file
    f.close()
    # Display a message to the user
    print('Record not found.')

# delete a record from and remove the record from the file
# read the whole file into a list or array
# delete the record from the list
# open the file for writing
# write the file without the deleted record in the list
def delete_record2():
    # Get the ID to delete
    student_id = int(input('Enter student ID: '))

    # Open the file and read the whole file into a list
    with open('students.dat', 'rb') as f:
        records = f.readlines()
    # Close the file
    f.close()

    # Loop through the list
    for record in records:
        # Unpack the record
        id, name, fee = record_struct.unpack(record)
        # Check if the ID matches
        if id == student_id:
            # Remove the record from the list
            records.remove(record)
            # Open the file for writing
            with open('students.dat', 'wb') as f:
                # Write the list to the file
                f.writelines(records)
            # Display a message to the user
            print('Record deleted successfully.')
            # Close the file
            f.close()
            # Return from the function
            return

# Display the menu and get the user's choice
option = 0
while option != 7:
    print('1. Add a new record')
    print('2. Display all records')
    print('3. Search a record by ID')
    print('4. Modify a record by ID')
    print('5. Delete a record by ID.1 ')
    print('6. Delete a record by ID.2 ')
    print('7. Exit')
    option = int(input('Enter your choice: '))
    # Call the appropriate function
    if option == 1:
        add_record()
    elif option == 2:
        display_records()
    elif option == 3:
        search_record()
    elif option == 4:
        modify_record()
    elif option == 5:
        delete_record()
    elif option == 6:
        delete_record2()
    elif option == 7:
        print('Goodbye.')
        sys.exit()
    else:
        print('Invalid option.')
