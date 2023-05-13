"""
Task is to write code for binary direct access file using Struct library to read and write binary data
The code will use following hashing function to generate hash value for the key
the file will have 3 fields
1. employee id; integer
2. employee name; string
3. employee salary; float

the file will be created with 1000 records
where each record will have following number of bytes calculated using struct library
1. employee id; 4 bytes
2. employee name; 20 bytes
3. employee salary; 4 bytes
this way each record will have 28 bytes

we will use following hashing function to generate hash value for the key to store and retrieve the record
hash_value = key % 1000. this hashing function is called modulo hashing function and for clash resolution
we will use linear probing or open addressing/hashing or bucketing.

we will call the hasing function with key as employee id, like hash_value = hash_function(employee_id)

following operations will be performed on the file
1. create file
2. insert record
3. search record
4. update record
5. delete record
6. display all records
"""
# import struct library
import struct

def hash_function(key):
    return key % 1000

def create_file():
    # create file with 1000 records
    # each record will have 28 bytes
    # 4 bytes for employee id
    # 20 bytes for employee name
    # 4 bytes for employee salary

    # calculate the size of the file using struct library using following format
    # i for integer
    # 20s for string
    # f for float
    format = 'i20sf'
    size = struct.calcsize(format)

    # open file in binary write mode
    file = open('employee.dat', 'wb')

    # write 1000 records with default values that are 0
    for i in range(1000):
        file.write(struct.pack(format, 0, b'', 0.0)) 
        # b'' is used to create empty string
        # 0.0 is used to create float value
        # 0 is used to create integer value

    # close the file
    file.close()

def insert_record():
    # insert record in the file
    # ask user for employee id, employee name and employee salary
    # calculate hash value using hash_function
    # if the record is not present in the file at the calculated hash value location
    # write the record in the file
    # else
    # print record already exists

    # calculate the size of the file using struct library using following format
    # i for integer
    # 20s for string
    # f for float
    format = 'i20sf'
    size = struct.calcsize(format)

    try:
        # open file in binary read and write mode
        file = open('employee.dat', 'r+b')
    except FileNotFoundError:
        create_file()
        file = open('employee.dat', 'r+b')

    # ask user for employee id, employee name and employee salary
    employee_id = int(input('Enter employee id: '))
    employee_name = input('Enter employee name: ')
    employee_salary = float(input('Enter employee salary: '))

    # calculate hash value using hash_function
    hash_value = hash_function(employee_id)

    # read the record from the file
    file.seek(hash_value * size)
    record = file.read(size)

    # unpack the record
    id, name, salary = struct.unpack(format, record)

    # if the record is not present in the file
    if id == 0:
        # write the record in the file
        file.seek(hash_value * size)
        file.write(struct.pack(format, employee_id, employee_name.encode(), employee_salary))
    elif employee_id == id: #if the record is present in the file and has same id as entered by user
        # print record already exists
        print('Record already exists')
    else: #if the record is present in the file but has a different id then it is a clash
        # clash resolution using linear probing or open addressing/hashing or bucketing will be applied now
        # we will find the next empty location in the file and write the record there
        # we will use while loop to find the next empty location
        # we will use hash_value as the starting point for the while loop
        # we will increment hash_value by 1 in each iteration of the while loop
        while id != 0:
            hash_value = (hash_value + 1) % 1000
            file.seek(hash_value * size)
            record = file.read(size)
            id, name, salary = struct.unpack(format, record)

            # if the end of the file is reached then we will start from the beginning of the file
            if file.tell() == size * 1000:
                file.seek(0)
        # as we have reached to a location where the record is empty
        # we will write the record in the file
        file.seek(hash_value * size)
        file.write(struct.pack(format, employee_id, employee_name.encode(), employee_salary))


    # close the file
    file.close()

def search_record():
    # search record in the file
    # ask user for employee id
    # calculate hash value using hash_function
    # if the record is present in the file at the calculated hash value location
    # read the record from the file
    # else use while loop to find the record in the file
    # print record does not exist

    # calculate the size of the file using struct library using following format
    # i for integer
    # 20s for string
    # f for float
    format = 'i20sf'
    size = struct.calcsize(format)

    # open file in binary read and write mode
    file = open('employee.dat', 'rb')

    # ask user for employee id
    employee_id = int(input('Enter employee id: '))

    # calculate hash value using hash_function
    hash_value = hash_function(employee_id)

    # read the record from the file
    file.seek(hash_value * size)
    record = file.read(size)

    # unpack the record
    id, name, salary = struct.unpack(format, record)

    # if the record is present in the file
    if employee_id == id:
        # read the record from the file
        print('Employee id: ', id)
        print('Employee name: ', name.decode().strip())
        print('Employee salary: ', salary)
    else: # we will use while loop to find the record in the file
        # we move onwards from the hash_value location
        # and count the number of iterations so that we don't iterate more than 1000 times
        # if we iterate more than 1000 times then we will print record does not exist
        count = 0
        while employee_id != id: # linear probing or open addressing/hashing or bucketing
            hash_value = (hash_value + 1) % 1000
            file.seek(hash_value * size)
            record = file.read(size)
            id, name, salary = struct.unpack(format, record)
            count += 1
            if count == 1000:
                print('Record does not exists!!!')
                break

    # close the file
    file.close()

def update_record():
    # update record in the file
    # ask user for employee id
    # calculate hash value using hash_function
    # if the record is present in the file at the calculated hash value location
    # read the record from the file
    # ask user for new employee name and employee salary
    # update the record in the file
    # else use while loop to find the record in the file
    # print record does not exist

    # calculate the size of the file using struct library using following format
    # i for integer
    # 20s for string
    # f for float
    format = 'i20sf'
    size = struct.calcsize(format)

    # open file in binary read and write mode
    file = open('employee.dat', 'r+b')

    # ask user for employee id
    employee_id = int(input('Enter employee id: '))

    # calculate hash value using hash_function
    hash_value = hash_function(employee_id)

    # read the record from the file
    file.seek(hash_value * size)
    record = file.read(size)

    # unpack the record
    id, name, salary = struct.unpack(format, record)

    # if the record is present in the file
    if employee_id == id:
        # read the record from the file
        print('Employee id: ', id)
        print('Employee name: ', name.decode().strip())
        print('Employee salary: ', salary)
        # ask user for new employee name and employee salary
        new_employee_name = input('Enter new employee name: ')
        new_employee_salary = float(input('Enter new employee salary: '))
        # update the record in the file
        file.seek(hash_value * size)
        file.write(struct.pack(format, employee_id, new_employee_name.encode(), new_employee_salary))
    else: # we will use while loop to find the record in the file
        # we move onwards from the hash_value location
        # and count the number of iterations so that we don't iterate more than 1000 times
        # if we iterate more than 1000 times then we will print record does not exist
        count = 0
        flag = True # flag to check if the record is found or not
        while employee_id != id: # linear probing or open addressing/hashing or bucketing
            hash_value = (hash_value + 1) % 1000
            file.seek(hash_value * size)
            record = file.read(size)
            id, name, salary = struct.unpack(format, record)
            count += 1
            if count == 1000:
                flag = False
                print('Record does not exists!!!')
                break
        if flag:
            # read the record from the file
            print('Employee id: ', id)
            print('Employee name: ', name.decode().strip())
            print('Employee salary: ', salary)
            # ask user for new employee name and employee salary
            new_employee_name = input('Enter new employee name: ')
            new_employee_salary = float(input('Enter new employee salary: '))
            # update the record in the file
            file.seek(hash_value * size)
            file.write(struct.pack(format, employee_id, new_employee_name.encode(), new_employee_salary))
            print('Record updated successfully!!!')

    # close the file
    file.close()

def delete_record():
    # delete record in the file
    # ask user for employee id
    # calculate hash value using hash_function
    # if the record is present in the file at the calculated hash value location
    # read the record from the file
    # ask user for confirmation to delete the record
    # if the user enters y then delete the record
    # else do not delete the record
    # else use while loop to find the record in the file
    # print record does not exist

    # calculate the size of the file using struct library using following format
    # i for integer
    # 20s for string
    # f for float
    format = 'i20sf'
    size = struct.calcsize(format)

    # open file in binary read and write mode
    file = open('employee.dat', 'r+b')

    # ask user for employee id
    employee_id = int(input('Enter employee id: '))

    # calculate hash value using hash_function
    hash_value = hash_function(employee_id)

    # read the record from the file
    file.seek(hash_value * size)
    record = file.read(size)

    # unpack the record
    id, name, salary = struct.unpack(format, record)

    # if the record is present in the file
    if employee_id == id:
        # read the record from the file
        print('Employee id: ', id)
        print('Employee name: ', name.decode().strip())
        print('Employee salary: ', salary)
        # ask user for confirmation to delete the record
        confirmation = input('Are you sure you want to delete this record? (y/n): ')
        # if the user enters y then delete the record
        if confirmation == 'y':
            # update the record in the file
            file.seek(hash_value * size)
            file.write(struct.pack(format, 0, ' '.encode(), 0))
            print('Record deleted successfully!!!')
    else: # we will use while loop to find the record in the file
        # we move onwards from the hash_value location
        # and count the number of iterations so that we don't iterate more than 1000 times
        # if we iterate more than 1000 times then we will print record does not exist
        count = 0
        flag = True # flag to check if the record is found or not
        while employee_id != id: # linear probing or open addressing/hashing or bucketing
            hash_value = (hash_value + 1) % 1000
            file.seek(hash_value * size)
            record = file.read(size)
            id, name, salary = struct.unpack(format, record)
            count += 1
            if count == 1000:
                flag = False
                print('Record does not exists!!!')
                break
        if flag:
            # read the record from the file
            print('Employee id: ', id)
            print('Employee name: ', name.decode().strip())
            print('Employee salary: ', salary)
            # ask user for confirmation to delete the record
            confirmation = input('Are you sure you want to delete this record? (y/n): ')
            # if the user enters y then delete the record
            if confirmation == 'y':
                # update the record in the file
                file.seek(hash_value * size)
                file.write(struct.pack(format, 0, ' '.encode(), 0))
                print('Record deleted successfully!!!')
    # close the file
    file.close()

def display_all_records():
    # display all records in the file
    # open file in binary read mode
    # read all the records from the file
    # unpack the records
    # print the records

    # calculate the size of the file using struct library using following format
    # i for integer
    # 20s for string
    # f for float
    format = 'i20sf'
    size = struct.calcsize(format)

    # open file in binary read mode
    file = open('employee.dat', 'rb')

    # read all the records from the file
    # and save it in records array or list
    records = file.read()

    # unpack the records
    for i in range(0, len(records), size):
        record = records[i:i+size]
        id, name, salary = struct.unpack(format, record)
        if id != 0:
            # print the records
            print('Employee id: ', id)
            print('Employee name: ', name.decode().strip())
            print('Employee salary: ', salary)
            print()
    # close the file
    file.close()

# main code for the menu driven approach
option = 0 # option to select the operation from menu

while True:
    print('1. Add record')
    print('2. Search record')
    print('3. Update record')
    print('4. Delete record')
    print('5. Display all records')
    print('6. Create binary direct access file')
    print('7. Exit')
    option = int(input('Enter option: '))
    if option == 1:
        insert_record()
    elif option == 2:
        search_record()
    elif option == 3:
        update_record()
    elif option == 4:
        delete_record()
    elif option == 5:
        display_all_records()
    elif option == 6:
        create_file()
    elif option == 7:
        break
    else:
        print('Invalid option!!!')

# End of program