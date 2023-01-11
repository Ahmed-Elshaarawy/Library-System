from Books import Book
from Library import *

class User:
    def __init__(self, name, ID, email):
        self._name = name
        self._ID = ID
        self._email = email

    # getters
    @property
    def name(self):
        return self._name

    @property
    def ID(self):
        return self._ID

    @property
    def email(self):
        return self._email


    # Setters
    @name.setter
    def name(self, name):
        self._name = name


    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @email.setter
    def email(self, email):
        self._email = email

    def __repr__(self):
        return f'User name: {self.name}\n' \
               f'User ID: {self.email}\n' \
               f'User email: {self.ID}\n' \
               f'User email: {self.ID}\n'

    def __eq__(self, other):
        if isinstance(other, type(self)):
            if self.name == other.name and self.ID == other.ID:
                return True
            else:
                return False
        else:
            return False

    def __dict__(self):
        return {
            "name": self.name,
            "email": self.email,
            "id": self.ID
        }


class Student(User):
    def __init__(self, name, ID, email, borrowedBooks=None):
        super(Student, self).__init__(name, ID, email)
        self._borrowedBooks = borrowedBooks

    # def __repr__(self):
        # represent = "Student(" + self.name + "," + self.municipality + "," + str(self.social_number) + ")"
        # return represent

    @property
    def borrowedBooks(self):
        return self._borrowedBooks

    @borrowedBooks.setter
    def borrowedBooks(self, borrowedBooks):
        self._borrowedBooks = borrowedBooks

    def borrowBook(self, book: Book):
        self.borrowedBooks.append(book)

    def returnBook(self, book: Book):
        try:
            self.borrowedBooks.remove(book)
        except ValueError:
            return "Book not in the borrow list! Can't be removed!"

    def __dict__(self):
        return {
            "name": self.name,
            "email": self.email,
            "id": self.ID,
            "borrowedBooks":self.borrowedBooks
        }

    def __repr__(self):
        return super().__repr__() + f'list of books borrowed is: {self.borrowedBooks}'


class Librarian(User):
    def __init__(self, name, ID, email, affLibrs: list ):
        super(Librarian, self).__init__(name, ID, email)
        self.affLibrs = affLibrs

    def addBook(self, book: Book, booksList: list):
        booksList.append(book)

    def removeBook(self, book: Book, booksList: list):
        try:
            self.bookList.remove(book)
        except ValueError:
            return "the book is not in the books list! Can't be removed!"

    # def searchBook(self, book: Book, booksList: list):
    #     try:
    #         return booksList.index(book)
    #     except ValueError:
    #         return "Book not found!"
    def __dict__(self):
        return {
            "name": self.name,
            "email": self.email,
            "id": self.ID,
            "libraries": self.affLibrs,

        }

    def __repr__(self):
        return super().__repr__() + f'list of libraries he is affiliated with is: {self.affLibrs}'


class Admin(User):
    def __init__(self, name, ID, email, affLibrs = []):
        super(Admin, self).__init__(name, ID, email)
        self.affLibrs = affLibrs

    def addUser(self, user: User,SchoolList: list):
        SchoolList.append(user)

    def removeUser(self, user: User, SchoolList: list):
        try:
            SchoolList.remove(user)
        except ValueError:
            return "the User is not in the users list! Can't be removed!"

    def __dict__(self):
        return {
            "name":self.name,
            "email":self.email,
            "id":self.ID,
            "libraries":self.affLibrs,

        }

    def __repr__(self):
        return super().__repr__() + f'list of libraries he is affiliated with is: {self.affLibrs}'


class Regular(User):
    def __init__(self, name, ID, email, address, age, social_number,  borrowedBooks=[]):
        super(Regular, self).__init__(name, ID, email)
        self._age = age
        self._address = address
        self._social_number = social_number
        self._borrowedBooks = borrowedBooks

    #  getter
    @property
    def age(self):
        return self.age

    @property
    def address(self):
        return self.address

    @property
    def social_number(self):
        return self.social_number

    @property
    def borrowedBooks(self):
        return self._borrowedBooks

    @borrowedBooks.setter
    def borrowedBooks(self, borrowedBooks):
        self._borrowedBooks = borrowedBooks


    # setter
    @age.setter
    def age(self, age):
        self._age = age

    @address.setter
    def address(self, address):
        self.address = address

    @social_number.setter
    def social_number(self, social_number):
        self._social_number = social_number


    def borrowBook(self, book: Book):
        self.borrowedBooks.append(book)

    def returnBook(self, book: Book):
        try:
            self.borrowedBooks.remove(book)
        except ValueError:
            return "Book not in the borrow list! Can't be removed!"

    def __dict__(self):
        return {
            "name": self.name,
            "email": self.email,
            "id": self.ID,
            "borrowedBooks":self.borrowedBooks,
            "address":self.address,
            "social number":self._social_number
        }


class CreditCard:

    def __init__(self):
        """ initialize the current_balance """
        self.current_balance = 0 #initialize current balance
        self.available_credit = 10000 #initialize available credit


    def getBalance(self):
        """ return the current_balance """
        return self.current_balance

    def getAvailableCredit(self):
        """ return the available_credit """
        return self.available_credit
