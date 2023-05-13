import pickle
import os
import sys

# Add a new record
def add_record():
    # Get the data from the user
    student_id = int(input('Enter student ID: '))
    student_name = input('Enter student name: ')
    student_fee = float(input('Enter student fee: '))

    # Create a dictionary for the record
    record = {
        'id': student_id,
        'name': student_name,
        'fee': student_fee
    }

    # Open the file in binary mode
    with open('studentsPickle.dat', 'ab') as f:
        # Serialize and write the record to the file
        pickle.dump(record, f)

    # Display a message to the user
    print('Record added successfully.')

# Display all records
def display_records():
    # Open the file in binary mode
    with open('studentsPickle.dat', 'rb') as f:
        try:
            while True:
                # Deserialize and load the record from the file
                record = pickle.load(f)
                # Display the record
                print('Student ID:', record['id'])
                print('Student Name:', record['name'])
                print('Student Fee:', record['fee'])
                print()
        except EOFError:
            pass

# Search a record by ID
def search_record():
    # Get the ID to search for
    student_id = int(input('Enter student ID: '))

    # Open the file in binary mode
    with open('studentsPickle.dat', 'rb') as f:
        try:
            while True:
                # Deserialize and load the record from the file
                record = pickle.load(f)
                # Check if the ID matches
                if record['id'] == student_id:
                    # Display the record
                    print('Student ID:', record['id'])
                    print('Student Name:', record['name'])
                    print('Student Fee:', record['fee'])
                    print()
                    return
        except EOFError:
            pass

    # Display a message to the user if the record is not found
    print('Record not found.')

# Modify a record by ID
def modify_record():
    # Get the ID to modify
    student_id = int(input('Enter student ID: '))

    # Open the file in binary mode
    with open('studentsPickle.dat', 'rb+') as f:
        try:
            while True:
                # Get the current file position
                position = f.tell()
                # Deserialize and load the record from the file
                record = pickle.load(f)
                # Check if the ID matches
                if record['id'] == student_id:
                    # Get the new data from the user
                    student_name = input('Enter student name: ')
                    student_fee = float(input('Enter student fee: '))

                    # Update the record
                    record['name'] = student_name
                    record['fee'] = student_fee

                    # Move the file position back to the beginning of the record
                    f.seek(position)
                    # Serialize and write the modified record to the file
                    pickle.dump(record, f)
                    # Display a message to the user
                    print('Record modified successfully.')
                    return
        except EOFError:
            pass

    # Display a message to the user if the record is not found
    print('Record not found.')

# Delete a record by ID
def delete_record():
    # Get the ID to delete
    student_id = int(input('Enter student ID: '))

    # Create a temporary file
    temp_file = 'temp.dat'

    # Open the files in binary mode
    with open('studentsPickle.dat', 'rb') as f, open(temp_file, 'wb') as temp_f:
        try:
            while True:
                # Deserialize and load the record from the file
                record = pickle.load(f)
                # Check if the ID matches
                if record['id'] == student_id:
                    # Skip the record to effectively delete it
                    continue
                # Serialize and write the record to the temporary file
                pickle.dump(record, temp_f)
        except EOFError:
            pass

    # Close the files
    f.close()
    temp_f.close()

    # Replace the original file with the temporary file
    os.remove('studentsPickle.dat')
    os.rename(temp_file, 'studentsPickle.dat')

    # Display a message to the user
    print('Record deleted successfully.')

# Display the menu and get the user's choice
option = 0
while option != 6:
    print('1. Add a new record')
    print('2. Display all records')
    print('3. Search a record by ID')
    print('4. Modify a record by ID')
    print('5. Delete a record by ID')
    print('6. Exit')
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
        print('Goodbye.')
        sys.exit()
    else:
        print('Invalid option.')
# end of program