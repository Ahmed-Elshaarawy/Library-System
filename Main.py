# ------------------------------------------------
# Assignment2
# Written by: Ahmed ELshaarawy , ID: 202100615
# -----------------------------------------------------

from Library import *
from School_library import *
from Municipal_library import *
from Books import *
from search_func import *
from typing import List
from national_library import *
from User import *


user = User('as', 2121, 'agag@.ca')
school = onlineSchool_library()
national = national_Library()
municipial = municipial_library()
L = library()


user = Student("ahmed", 2021, "am@upei.ca")
# school.registerd_user(user)
# school.add_user_to_restricted(user)

user = Regular("a", 1101,'as@ryerson.ca', 22, 'giza', 22121)
school.add_user(user)

user = Student("ahmed1", 20211, "am@upei.ca1","ca")



#  should be changed to reading from a file
bookList = [Book("python 4everyone", "Horstmann", '978-1-119-49853-7', 2, 0, 0, 15, []),
            Book("absolute Java", "Savitch", '9780134041674', 3, 0, 0, 15, [])]

SchoolList = [[User("Ali", 1010, 'ali@gmail.com'), '1234'],
            [Student("Ahmed", 00000, 'aaa@bbb.com', []), '4532'],
            [Student("Shadi", 1111, 'Shadi@bbb.com', []), '5678'],
            [Librarian("Morris", 2222, 'Moris@bbb.com', ["UPEI", "Ryerson"]), 'lglg'],
            [Admin("David", 3333, 'Dave@bbb.com', ["UPEI", "Ryerson"]), 'pppp']]



all_users = {"users": []}
data_holder = all_users["users"]
with open('data.json', 'w') as f:
    for i, user in enumerate(SchoolList):
        data = {"user_data": user[0].__dict__(), "type": user[0].__class__.__name__}
        data_holder.append(data)
    json_string = json.dumps(all_users, indent=4)
    f.write(json_string)


municipialList = [[User("MO", 1122, 'MO@gmail.com'), '123'],
            [Librarian("AH", 44444, 'AH@bbb.com', []), '321'],
            [Regular("XA", 3333, 'XA@bbb.com', 'giza',20, 666), '12345'],
            [Admin("A", 8888, 'A@bbb.com', []), '777']]

all_users = {"users": []}
data_holder = all_users["users"]
with open('data.json', 'w') as f:
    for i, user in enumerate(municipialList):
        data = {"user_data": user[0].__dict__(), "type": user[0].__class__.__name__}
        data_holder.append(data)
    json_string = json.dumps(all_users, indent=4)
    f.write(json_string)

nationalList = [[User("MS", 3322, 'MS@gmail.com'), '654'],
            [Librarian("XZ", 5555, 'XZ@bbb.com', ["UPEI", "Ryerson"]), '987'],
            [Regular("SS", 999, 'SS@bbb.com', 'giza',22, 99959), '123456'],
            [Admin("D", 000, 'D@bbb.com', []), '2000']]

all_users = {"users": []}
data_holder = all_users["users"]
with open('data.json', 'w') as f:
    for i, user in enumerate(nationalList):
        data = {"user_data": user[0].__dict__(), "type": user[0].__class__.__name__}
        data_holder.append(data)
    json_string = json.dumps(all_users, indent=4)
    f.write(json_string)

# with open('data.json', 'r') as openfile:
#     # Reading from json file
#     json_object = json.load(openfile)
#
# users_data = []
# for data in json_object["SchoolList"]:
#     if data["type"] == 'Student':
#         users_data.append(Student(**data["user_data"]))
#
# users_data = []
# for data in json_object["municipialList"]:
#     if data["type"] == 'Regular':
#         users_data.append(Regular(**data["user_data"]))
#
# users_data = []
# for data in json_object["nationalList"]:
#     if data["type"] == 'Regular':
#         users_data.append(Regular(**data["user_data"]))

menu = input("Dear user choose which library type you want to login in it \n"
             "1) School library \n"
             "2) Municipial LIBRARY \n"
             "3) National library")

if int(menu) == 1:
    username, password = input("Please enter your username and password").split()
    # username = input("Please enter your username and password")
    # password = input("Please enter your username and password")

    # search the user and display his menu based on his type
    foundIndex = -1
    for i, user in enumerate(SchoolList):
        # check if the user exists in the DB(data_base)
        # print(user)
        if user[0].name == username:
            # check if his password matches the password
            if user[1] == password:
                foundIndex = i
                print(f"found at {foundIndex}")

    # display menus based on the user type and whether he is found or not
    if foundIndex >= 0:
        if isinstance(SchoolList[foundIndex][0], Student):
            print("found again")
            Choice = input('Dear user your options are:\n'
                               '1) Borrow a book\n'
                               '2) return a book\n'
                               '3) search for a book\n')
        elif isinstance(SchoolList[foundIndex][0], Librarian):
            Choice = input('Dear Librarian your options are:\n'
                               '1) Add a book\n'
                               '2) Remove a book\n'
                               '3) search for a book\n')
        elif isinstance(SchoolList[foundIndex][0], Admin):
            Choice = input('Dear Admin your options are:\n'
                               '1) Add a user\n'
                               '2) Remove a user\n'
                               '3) search for a book')

    # Student user operations
    if isinstance(SchoolList[foundIndex][0], Student):
        # borrow a book choice
        if int(Choice) == 1:
            # ask the user for the bookname he wants to borrow
            bookToBorrow = input("enter the title of the book to borrow?")
            # seacrh for the book in the bookList
            bookIndex = searchForBook(bookToBorrow, bookList)
            print(bookIndex)
            # add the book to the list of books the user borrowing, if available
            if bookIndex >= 0:
                # add the book to the user account
                SchoolList[foundIndex][0].borrowBook(bookList[bookIndex])
                print("Book added to user account successfully!")
                # print(SchoolList[foundIndex][0])
                # update book record
                bookList[bookIndex].noOfCpsBorrowed += 1
                bookList[bookIndex].borrowers.append(SchoolList[foundIndex][0])
                print(bookList[bookIndex].borrowers)
            else:
                print("sorry book not found!")
        # return a book choice
        if int(Choice) == 2:
            # ask the user for the bookname he wants to return
            bookToReturn = input("enter the title of the book to return?")
            # remove the book from the user account
            try:
                # remove it from the user list of borrowed books
                SchoolList[foundIndex][0].returnBook(bookList[bookIndex])
                # update the number of borrowed copies for this book
                bookList[bookIndex].noOfCpsBorrowed -= 1
            except:
                print("Book is not borrowed by this user! Cannot be returned")
        # search for a book choice
        if int(Choice) == 3:
            # ask the user for the bookname he wants to borrow
            bookToSearch = input("enter the title of the book to search for?")
            # seacrh for the book in the bookList
            bookIndex = searchForBook(bookToSearch, bookList)
            if bookIndex >= 0:
                print("the requested book details:\n")
                print(bookList[bookIndex])
            else:
                print("Sorry, this book is not found in the library!")

    # Librarian user operations
    if isinstance(SchoolList[foundIndex][0], Librarian):
        # Add a book choice
        if int(Choice) == 1:
            bookDetails: List[str] = input("please enter the details of the book in CSV format").split(',')
            bookList.append(Book(bookDetails[0], bookDetails[1], bookDetails[2], bookDetails[3],
                                 bookDetails[4], bookDetails[5], bookDetails[6], bookDetails[7]))
        # Remove a book choice
        if int(Choice) == 2:
            # ask the librarian for the book name he wants to remove
            bookToRemove = input("enter the title of the book to remove from the list?")
            # search for the book in the bookList
            bookIndex = searchForBook(bookToRemove, bookList)
            try:
                SchoolList[foundIndex][0].remove(bookList[bookIndex], bookList)
            except:
                print("the book is not in the books list! Can't be removed!")

        if int(Choice) == 3:
            # ask the libraian for the book name he wants to borrow
            bookToSearch = input("enter the title of the book to search for?")
            # seacrh for the book in the bookList
            bookIndex = searchForBook(bookToSearch, bookList)
            if bookIndex >= 0:
                print("the requested book details:\n")
                print(bookList[bookIndex])
            else:
                print("Sorry, this book is not found in the library!")
    # Admin user operations
    if isinstance(SchoolList[foundIndex][0], Admin):
        # add user to the list
        if int(Choice) == 1:
            userDetails = input("please enter the new user details in CSV format:").split(',')
            userType = int(input("what type of user: 1) normal, 2) Librarian, 3) Admin"))
            if userType == 1:
                SchoolList.append([Student(userDetails[0], userDetails[1], userDetails[2]),'1234'])
            elif userType == 2:
                SchoolList.append([Librarian(userDetails[0], userDetails[1], userDetails[2]),'324'])
            elif userType == 3:
                SchoolList.append([Admin(userDetails[0], userDetails[1], userDetails[2]), '4545'])
            print(SchoolList[-1])
        # remove user to the list
        if int(Choice) == 2:
            # ask the admin for the user he wants to remove
            userToRemove = input("enter the name of the user to remove from the list?")
            # search for the book in the bookList
            userIndex = searchForUser(userToRemove, SchoolList)
            try:
                SchoolList.pop(userIndex)
            except:
                print("the user is not in the users list! Can't be removed!")

        if int(Choice) == 3:
            bookToSearch = input("enter the title of the book to search for?")
            # seacrh for the book in the bookList
            bookIndex = searchForBook(bookToSearch, bookList)
            if bookIndex >= 0:
                print("the requested book details:\n")
                print(bookList[bookIndex])
            else:
                print("Sorry, this book is not found in the library!")


if int(menu) == 2:
    username, password = input("Please enter your username and password").split()
    # search the user and display his menu based on his type
    foundIndex = -1
    for i, user in enumerate(municipialList):
        # check if the user exists in the DB(data_base)
        # print(user)
        if user[0].name == username:
            # check if his password matches the password
            if user[1] == password:
                foundIndex = i
                print(f"found at {foundIndex}")

    # display menus based on the user type and whether he is found or not
    if foundIndex >= 0:
        if isinstance(municipialList[foundIndex][0], Regular):
            print("found again")
            Choice = input('Dear user your options are:\n'
                               '1) Borrow a book\n'
                               '2) return a book\n'
                               '3) search for a book\n')
        elif isinstance(municipialList[foundIndex][0], Librarian):
            Choice = input('Dear Librarian your options are:\n'
                               '1) Add a book\n'
                               '2) Remove a book\n'
                               '3) search for a book\n')
        elif isinstance(municipialList[foundIndex][0], Admin):
            Choice = input('Dear Admin your options are:\n'
                               '1) Add a user\n'
                               '2) Remove a user\n'
                               '3) search for a book')

    # regular user operations
    if isinstance(municipialList[foundIndex][0], Regular):
        # borrow a book choice
        if int(Choice) == 1:
            # ask the user for the bookname he wants to borrow
            bookToBorrow = input("enter the title of the book to borrow?")
            # seacrh for the book in the bookList
            bookIndex = searchForBook(bookToBorrow, bookList)
            # add the book to the list of books the user borrowing, if available
            if bookIndex >= 0:
                # add the book to the user account
                municipialList[foundIndex][0].borrowBook(bookList[bookIndex])
                print("Book added to user account successfully!")
                # print(SchoolList[foundIndex][0])
                # update book record
                bookList[bookIndex].noOfCpsBorrowed += 1
                bookList[bookIndex].borrowers.append(municipialList[foundIndex][0])
                print(bookList[bookIndex].borrowers)
            else:
                print("sorry book not found!")
        # return a book choice
        if int(Choice) == 2:
            # ask the user for the bookname he wants to return
            bookToReturn = input("enter the title of the book to return?")
            # remove the book from the user account
            try:
                # remove it from the user list of borrowed books
                municipialList[foundIndex][0].returnBook(bookList[bookIndex])
                # update the number of borrowed copies for this book
                bookList[bookIndex].noOfCpsBorrowed -= 1
            except:
                print("Book is not borrowed by this user! Cannot be returned")
        # search for a book choice
        if int(Choice) == 3:
            # ask the user for the bookname he wants to borrow
            bookToSearch = input("enter the title of the book to search for?")
            # seacrh for the book in the bookList
            bookIndex = searchForBook(bookToSearch, bookList)
            if bookIndex >= 0:
                print("the requested book details:\n")
                print(bookList[bookIndex])
            else:
                print("Sorry, this book is not found in the library!")

    # Librarian user operations
    if isinstance(municipialList[foundIndex][0], Librarian):
        # Add a book choice
        if int(Choice) == 1:
            bookDetails: List[str] = input("please enter the details of the book in CSV format").split(',')
            bookList.append(Book(bookDetails[0], bookDetails[1], bookDetails[2], bookDetails[3],
                                 bookDetails[4], bookDetails[5], bookDetails[6], bookDetails[7]))
        # Remove a book choice
        if int(Choice) == 2:
            # ask the librarian for the book name he wants to remove
            bookToRemove = input("enter the title of the book to remove from the list?")
            # search for the book in the bookList
            bookIndex = searchForBook(bookToRemove, bookList)
            try:
                municipialList[foundIndex][0].remove(bookList[bookIndex], bookList)
            except:
                print("the book is not in the books list! Can't be removed!")

        if int(Choice) == 3:
            bookToSearch = input("enter the title of the book to search for?")
            # seacrh for the book in the bookList
            bookIndex = searchForBook(bookToSearch, bookList)
            if bookIndex >= 0:
                print("the requested book details:\n")
                print(bookList[bookIndex])
            else:
                print("Sorry, this book is not found in the library!")

    # Admin user operations
    if isinstance(municipialList[foundIndex][0], Admin):
        # add user to the list
        if int(Choice) == 1:
            userDetails = input("please enter the new user details in CSV format:").split(',')
            userType = int(input("what type of user: 1) Regular, 2) Librarian, 3) Admin"))
            if userType == 1:
                municipialList.append([Regular(userDetails[0], userDetails[1], userDetails[2], userDetails[3], userDetails[4], userDetails[5]), 'jdjd'])
            elif userType == 2:
                municipialList.append([Librarian(userDetails[0], userDetails[1], userDetails[2]), 'fsdf'])
            elif userType == 3:
                municipialList.append([Admin(userDetails[0], userDetails[1], userDetails[2]), 'ffsd'])
            print(municipialList[-1])
        # remove user to the list
        if int(Choice) == 2:
            # ask the admin for the user he wants to remove
            userToRemove = input("enter the name of the user to remove from the list?")
            # search for the book in the bookList
            userIndex = searchForUser(userToRemove, municipialList)
            try:
                municipialList.pop(userIndex)
            except:
                print("the user is not in the users list! Can't be removed!")

        if int(Choice) == 3:
            bookToSearch = input("enter the title of the book to search for?")
            # seacrh for the book in the bookList
            bookIndex = searchForBook(bookToSearch, bookList)
            if bookIndex >= 0:
                print("the requested book details:\n")
                print(bookList[bookIndex])
            else:
                print("Sorry, this book is not found in the library!")

if int(menu) == 3:
    username, password = input("Please enter your username and password").split()
    # search the user and display his menu based on his type
    foundIndex = -1
    for i, user in enumerate(nationalList):
        # check if the user exists in the DB(data_base)
        # print(user)
        if user[0].name == username:
            # check if his password matches the password
            if user[1] == password:
                foundIndex = i
                print(f"found at {foundIndex}")

    # display menus based on the user type and whether he is found or not
    if foundIndex >= 0:
        if isinstance(nationalList[foundIndex][0], Regular):
            print("found again")
            Choice = input('Dear user your options are:\n'
                               '1) Borrow a book\n'
                               '2) return a book\n'
                               '3) search for a book\n')
        elif isinstance(nationalList[foundIndex][0], Librarian):
            Choice = input('Dear Librarian your options are:\n'
                               '1) Add a book\n'
                               '2) Remove a book\n'
                               '3) search for a book\n')
        elif isinstance(nationalList[foundIndex][0], Admin):
            Choice = input('Dear Admin your options are:\n'
                               '1) Add a user\n'
                               '2) Remove a user\n'
                               '3) search for a book')

    # regular user operations
    if isinstance(nationalList[foundIndex][0], Regular):
        # borrow a book choice
        if int(Choice) == 1:
            # ask the user for the bookname he wants to borrow
            bookToBorrow = input("enter the title of the book to borrow?")
            # seacrh for the book in the bookList
            bookIndex = searchForBook(bookToBorrow, bookList)
            # add the book to the list of books the user borrowing, if available
            if bookIndex >= 0:
                # add the book to the user account
                nationalList[foundIndex][0].borrowBook(bookList[bookIndex])
                print("Book added to user account successfully!")
                # update book record
                bookList[bookIndex].noOfCpsBorrowed += 1
                bookList[bookIndex].borrowers.append(nationalList[foundIndex][0])
                print(bookList[bookIndex].borrowers)
            else:
                print("sorry book not found!")
        # return a book choice
        if int(Choice) == 2:
            # ask the user for the bookname he wants to return
            bookToReturn = input("enter the title of the book to return?")
            # remove the book from the user account
            try:
                # remove it from the user list of borrowed books
                nationalList[foundIndex][0].returnBook(bookList[bookIndex])
                # update the number of borrowed copies for this book
                bookList[bookIndex].noOfCpsBorrowed -= 1
            except:
                print("Book is not borrowed by this user! Cannot be returned")
        # search for a book choice
        if int(Choice) == 3:
            # ask the user for the bookname he wants to borrow
            bookToSearch = input("enter the title of the book to search for?")
            # seacrh for the book in the bookList
            bookIndex = searchForBook(bookToSearch, bookList)
            if bookIndex >= 0:
                print("the requested book details:\n")
                print(bookList[bookIndex])
            else:
                print("Sorry, this book is not found in the library!")

    # Librarian user operations
    if isinstance(nationalList[foundIndex][0], Librarian):
        # Add a book choice
        if int(Choice) == 1:
            bookDetails: List[str] = input("please enter the details of the book in CSV format").split(',')
            bookList.append(Book(bookDetails[0], bookDetails[1], bookDetails[2], bookDetails[3],
                                 bookDetails[4], bookDetails[5], bookDetails[6], bookDetails[7]))
        # Remove a book choice
        if int(Choice) == 2:
            # ask the librarian for the book name he wants to remove
            bookToRemove = input("enter the title of the book to remove from the list?")
            # search for the book in the bookList
            bookIndex = searchForBook(bookToRemove, bookList)
            try:
                nationalList[foundIndex][0].remove(bookList[bookIndex], bookList)
            except:
                print("the book is not in the books list! Can't be removed!")

        if int(Choice) == 3:
            bookToSearch = input("enter the title of the book to search for?")
            # seacrh for the book in the bookList
            bookIndex = searchForBook(bookToSearch, bookList)
            if bookIndex >= 0:
                print("the requested book details:\n")
                print(bookList[bookIndex])
            else:
                print("Sorry, this book is not found in the library!")

    # Admin user operations
    if isinstance(nationalList[foundIndex][0], Admin):
        # add user to the list
        if int(Choice) == 1:
            userDetails = input("please enter the new user details in CSV format:").split(',')
            userType = int(input("what type of user: 1) Regular, 2) Librarian, 3) Admin"))
            if userType == 1:
                nationalList.append([Regular(userDetails[0], userDetails[1], userDetails[2], userDetails[3], userDetails[4], userDetails[5]), '11'])
            elif userType == 2:
                nationalList.append([Librarian(userDetails[0], userDetails[1], userDetails[2]), '22'])
            elif userType == 3:
                nationalList.append([Admin(userDetails[0], userDetails[1], userDetails[2]), '55'])
            print(nationalList[-1])
        # remove user to the list
        if int(Choice) == 2:
            # ask the admin for the user he wants to remove
            userToRemove = input("enter the name of the user to remove from the list?")
            # search for the book in the bookList
            userIndex = searchForUser(userToRemove, nationalList)
            try:
                nationalList.pop(userIndex)
            except:
                print("the user is not in the users list! Can't be removed!")
        if int(Choice) == 3:
            bookToSearch = input("enter the title of the book to search for?")
            # seacrh for the book in the bookList
            bookIndex = searchForBook(bookToSearch, bookList)
            if bookIndex >= 0:
                print("the requested book details:\n")
                print(bookList[bookIndex])
            else:
                print("Sorry, this book is not found in the library!")
else:
    print()



all_users = {"users": []}
data_holder = all_users["users"]
with open('data.json', 'w') as f:
    for i, user in enumerate(SchoolList):
        data = {"user_data": user[0].__dict__(), "type": user[0].__class__.__name__}
        data_holder.append(data)
    json_string = json.dumps(all_users, indent=4)
    f.write(json_string)


all_users = {"users": []}
data_holder = all_users["users"]
with open('data.json', 'w') as f:
    for i, user in enumerate(municipialList):
        data = {"user_data": user[0].__dict__(), "type": user[0].__class__.__name__}
        data_holder.append(data)
    json_string = json.dumps(all_users, indent=4)
    f.write(json_string)

all_users = {"users": []}
data_holder = all_users["users"]
with open('data.json', 'w') as f:
    for i, user in enumerate(nationalList):
        data = {"user_data": user[0].__dict__(), "type": user[0].__class__.__name__}
        data_holder.append(data)
    json_string = json.dumps(all_users, indent=4)
    f.write(json_string)
