from User import *
import json
from Books import *

class library:

    bookname = ''

    def __init__(self, library_name="", library_type="", allowed_list_of_user_types=[],  registered_users=[],
                 restricted_users=[], books_in_library=[], borrowing_policy=[],  active_bookloans=[]):
        self._library_name = library_name
        self._library_type = library_type
        self._allowed_list_of_user_types = allowed_list_of_user_types
        self._registered_users = registered_users
        self._restricted_users = restricted_users
        self._books_in_library = books_in_library
        self._borrowing_policy = borrowing_policy
        self._active_bookloans = active_bookloans


    #getters
    @property
    def allowed_list_of_user_types(self):
        return self._allowed_list_of_user_types

    @property
    def restictedUsers(self):
        return self._restricted_users

    @property
    def registerd_user(self):
        return self._registered_users

    @property
    def active_bookloans(self):
        return self._active_bookloans



    #setters
    @registerd_user.setter
    def registerd_user(self, user):
        self.registerd_user.append(user)
    # def get_restrictedusers(self):
    #     return self._restricted_users

    @allowed_list_of_user_types.setter
    def allowed_list_of_user_types(self, allowed_list_of_user_types):
        self._allowed_list_of_user_types = allowed_list_of_user_types

    @restictedUsers.setter
    def restictedUsers(self, restictedUsers):
        self._restrict_user = restictedUsers

    @active_bookloans.setter
    def active_bookloans(self, book):
        self._active_bookloans = book



    # function to add book
    def add_book(self, bookname):
        self._books_in_library.append(bookname)

    # function to add user
    def add_user(self, user):
        self.registerd_user.append(user)

    # function to remove user
    def remove_user(self, user):
        self.registerd_user.pop(user)

    # function to see restricted users
    def restrict_user(self):
        self._restricted_users

    # func. to remove book
    def remove_book(self):
        self.books_in_library.pop()
        return self.books_in_library

    # func. to search for a book
    def searchBook(self, book: Book, booksList: list):
        try:
            return booksList.index(book)
        except ValueError:
            return "Book not found!"

    # func. to change borrowing policy
    def change_borrowingPolicy(self):
        print("")


