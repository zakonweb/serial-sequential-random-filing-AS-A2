"""
Task is to write code for binary direct access file using Pickle library to read and write binary data
The code will use following hashing function to generate hash value for the key
the file will have 3 fields
1. employee id; integer
2. employee name; string
3. employee salary; float

the file will be created with 1000 records
where each record will have following number of bytes calculated using Pickle library
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
import pickle

def hash_function(key):
    return key % 1000

def create_file():
    file = open('employeePickle.dat', 'wb')
    records = [(0, '', 0.0)] * 1000
    pickle.dump(records, file)
    file.close()

def insert_record():
    try:
        file = open('employeePickle.dat', 'rb')
        records = pickle.load(file)
        file.close()
    except FileNotFoundError:
        create_file()
        file = open('employeePickle.dat', 'rb')
        records = pickle.load(file)
        file.close()

    employee_id = int(input('Enter employee id: '))
    employee_name = input('Enter employee name: ')
    employee_salary = float(input('Enter employee salary: '))

    hash_value = hash_function(employee_id)

    record = records[hash_value]

    if record[0] == 0:
        records[hash_value] = (employee_id, employee_name, employee_salary)
    elif employee_id == record[0]:
        print('Record already exists')
    else:
        count = 0
        while record[0] != 0:
            hash_value = (hash_value + 1) % 1000
            record = records[hash_value]
            count += 1
            if count == 1000:
                print('Record does not exist!!!')
                break

        if record[0] == 0:
            records[hash_value] = (employee_id, employee_name, employee_salary)

    file = open('employeePickle.dat', 'wb')
    pickle.dump(records, file)
    file.close()

def search_record():
    file = open('employeePickle.dat', 'rb')
    records = pickle.load(file)
    file.close()

    employee_id = int(input('Enter employee id: '))

    hash_value = hash_function(employee_id)

    record = records[hash_value]

    if employee_id == record[0]:
        print('Employee id:', record[0])
        print('Employee name:', record[1].strip())
        print('Employee salary:', record[2])
    else:
        count = 0
        while record[0] != employee_id:
            hash_value = (hash_value + 1) % 1000
            record = records[hash_value]
            count += 1
            if count == 1000:
                print('Record does not exist!!!')
                break

        if record[0] == employee_id:
            print('Employee id:', record[0])
            print('Employee name:', record[1].strip())
            print('Employee salary:', record[2])

def update_record():
    file = open('employeePickle.dat', 'r+b')
    records = pickle.load(file)
    file.close()

    employee_id = int(input('Enter employee id: '))

    hash_value = hash_function(employee_id)

    record = records[hash_value]

    if employee_id == record[0]:
        print('Employee id:', record[0])
        print('Employee name:', record[1].strip())
        print('Employee salary:', record[2])
        new_employee_name = input('Enter new employee name: ')
        new_employee_salary = float(input('Enter new employee salary: '))
        records[hash_value] = (employee_id, new_employee_name, new_employee_salary)
    else:
        count = 0
        flag = True
        while record[0] != employee_id:
            hash_value = (hash_value + 1) % 1000
            record = records[hash_value]
            count += 1
            if count == 1000:
                flag = False
                print('Record does not exist!!!')
                break
        if flag:
            print('Employee id:', record[0])
            print('Employee name:', record[1].strip())
            print('Employee salary:', record[2])
            new_employee_name = input('Enter new employee name: ')
            new_employee_salary = float(input('Enter new employee salary: '))
            records[hash_value] = (employee_id, new_employee_name, new_employee_salary)
            print('Record updated successfully!!!')

    file = open('employeePickle.dat', 'wb')
    pickle.dump(records, file)
    file.close()

def delete_record():
    file = open('employeePickle.dat', 'r+b')
    records = pickle.load(file)
    file.close()

    employee_id = int(input('Enter employee id: '))

    hash_value = hash_function(employee_id)

    record = records[hash_value]

    if employee_id == record[0]:
        print('Employee id:', record[0])
        print('Employee name:', record[1].strip())
        print('Employee salary:', record[2])
        confirmation = input('Are you sure you want to delete this record? (y/n): ')
        if confirmation == 'y':
            records[hash_value] = (0, '', 0.0)
            print('Record deleted successfully!!!')
    else:
        count = 0
        flag = True
        while record[0] != employee_id:
            hash_value = (hash_value + 1) % 1000
            record = records[hash_value]
            count += 1
            if count == 1000:
                flag = False
                print('Record does not exist!!!')
                break
        if flag:
            print('Employee id:', record[0])
            print('Employee name:', record[1].strip())
            print('Employee salary:', record[2])
            confirmation = input('Are you sure you want to delete this record? (y/n): ')
            if confirmation == 'y':
                records[hash_value] = (0, '', 0.0)
                print('Record deleted successfully!!!')

    file = open('employeePickle.dat', 'wb')
    pickle.dump(records, file)
    file.close()

def display_all_records():
    file = open('employeePickle.dat', 'rb')
    records = pickle.load(file)
    file.close()

    for record in records:
        if record[0] != 0:
            print('Employee id:', record[0])
            print('Employee name:', record[1].strip())
            print('Employee salary:', record[2])
            print()

option = 0

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
# end of code