from User import *
from Library import *

class onlineSchool_library(library):
    def __int__(self, allowed_list_of_user_types,  registered_users, restricted_users,
                books_in_library, borrowing_policy,  active_bookloans):

        super(onlineSchool_library, self).__int__(allowed_list_of_user_types,  registered_users, restricted_users,
                books_in_library, borrowing_policy,  active_bookloans)


    def add_user(self,user):
        if not isinstance(user, Regular):
            return self._registered_users.append(user)
        else:
            print("You can't Enter the Library")

    def add_user_to_restricted(self,user):
        if not isinstance(user, Regular):
            self._restricted_users.append(user)
        else:
            print("The user can't be added to the restricted list")

    def borrowBook(self,bookname, user):
        if isinstance(user, Student):
            #if user in self.restictedUsers
            for userdata in self.restictedUsers:
                if userdata.name == user.name:
                    if not isinstance(user, self._restricted_users):
                        self._books_in_library.pop(bookname)
        else:
            print("sorry make sure you return the books you have borrowed before borrowing a new one.")

    def returnBook(self, bookname, user):
        if isinstance(user, Student):
            if not isinstance(user, self._restricted_users):
                self._books_in_library.append(bookname)
        else:
            print("sorry please try again to return the book")

