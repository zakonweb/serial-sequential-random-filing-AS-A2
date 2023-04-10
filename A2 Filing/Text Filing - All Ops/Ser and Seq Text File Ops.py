"""
code for serial text file that saves one record per line
the record consits of following fields:
student roll number, student name, student marks, student fee
the name of the file is studentataskari.txt
following are the functions to be implemented:
1. add a new record
2. search a record by roll number
3. edit a record by roll number
4. delete a record by roll number
5. display all records
6. make file sequential by roll number
7. exit
"""

def add_record():
    """
    input: roll number, name, marks, fee
    concatenate all the fields with comma as separator
    and append to the file
    """
    while True:
        # input the record
        roll = int(input("Enter roll number: "))
        if search_record(roll) is True:
            print("Record already exists")
        else:
            break
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    fee = float(input("Enter fee: "))

    # concatenate the record
    record = str(roll) + "," + name + "," + str(marks) + "," + str(fee)
    # alternatively use f string formatting
    # record = f"{roll},{name},{marks},{fee}"

    # open the file in append mode
    with open("studentataskari.txt", "at") as file:
        # write the record to the file
        file.write(record + "\n")
    
    # close the file
    file.close()

def search_record(rno=0):
    if rno != 0:
        roll = rno
    else:
        # input the roll number
        roll = int(input("Enter roll number to seach for: "))

    # flag to indicate if record is found
    found = False

    try:
        # open the file in read mode
        with open("studentataskari.txt", "rt") as file:
            # read each line from the file
            for line in file:
                # split the line into fields
                fields = line.split(",")
                # check if the roll number is found
                if int(fields[0]) == roll:
                    # set the flag
                    found = True
                    # print the record
                    print("Record found: ", line)
                    # close the file
                    file.close()
                    # return from the function
                    return True
            # if the record is not found
            if not found:
                # print the message
                print("Record not found")
        # close the file
        file.close()
    except FileNotFoundError:
        # print the message
        print("File not found")

def edit_record():
    # input the roll number
    roll = int(input("Enter roll number to edit: "))

    # flag to indicate if record is found
    found = False

    try:
        # open the file in read mode
        with open("studentataskari.txt", "rt") as file:
            # read the file into a list
            lines = file.readlines()

            # close the file
            file.close()

            # seach the list for the record
            for line in lines:
                record = line.split(",")
                if int(record[0]) == roll:
                    # set the flag
                    found = True

                    # input the new record
                    name = input("Enter new name: ")
                    marks = int(input("Enter new marks: "))
                    fee = float(input("Enter new fee: "))

                    # concatenate the new record
                    new_record = str(roll) + "," + name + "," + str(marks) + "," + str(fee)
                    # alternatively use f string formatting
                    # new_record = f"{roll},{name},{marks},{fee}"

                    # replace the old record with new record
                    lines[lines.index(line)] = new_record + "\n"

                    # open the file in write mode
                    with open("studentataskari.txt", "wt") as file:
                        # write the list to the file
                        file.writelines(lines)
                    # close the file
                    file.close()
            # if the record is not found
            if not found:
                # print the message
                print("Record not found")
    except FileNotFoundError:
        # print the message
        print("File not found")

def delete_record():
    # input the roll number to delete
    roll = int(input("Enter roll number to delete: "))

    # flag to indicate if record is found
    found = False

    try:
        # open the file in read mode
        with open("studentataskari.txt", "rt") as file:
            list = file.readlines()

            # close the file
            file.close()
        
        # search the list for the record
        for line in list:
            record = line.split(",")
            if int(record[0]) == roll:
                # set the flag
                found = True

                # remove the record from the list
                list.remove(line)

                # open the file in write mode
                with open("studentataskari.txt", "wt") as file:
                    # write the list to the file
                    file.writelines(list)
                # close the file
                file.close()

                # print the message
                print("Record deleted")

        # if the record is not found
        if not found:
            # print the message
            print("Record not found")
    except FileNotFoundError:
        # print the message
        print("File not found")

def display_records():
    try:
        # open the file in read mode
        print("All records: ")
        with open("studentataskari.txt", "rt") as file:
            # read each line from the file
            for line in file:
                # print the record
                print(line, end="")
        # close the file
        file.close()
        print("End of records")
    except FileNotFoundError:
        # print the message
        print("File not found")

def make_sequential():
    try:
        # open the file in read mode
        with open("studentataskari.txt", "rt") as file:
            # read the file into a list
            lines = file.readlines()

            # close the file
            file.close()

        # sort the list
        lines.sort()

        # open the file in write mode
        with open("studentataskari.txt", "wt") as file:
            # write the list to the file
            file.writelines(lines)
        # close the file
        file.close()

        # print the message
        print("File made sequential by roll number")
    except FileNotFoundError:
        # print the message
        print("File not found")

# main program
option = 0
while option != 7:
    print("1. Add a new record")
    print("2. Search a record by roll number")
    print("3. Edit a record by roll number")
    print("4. Delete a record by roll number")
    print("5. Display all records")
    print("6. Make file sequential by roll number")
    print("7. Exit")
    option = int(input("Enter your choice: "))
    if option == 1:
        add_record()
    elif option == 2:
        search_record()
    elif option == 3:
        edit_record()
    elif option == 4:
        delete_record()
    elif option == 5:
        display_records()
    elif option == 6:
        make_sequential()
    elif option == 7:
        print("Bye!")
    else:
        print("Invalid option")