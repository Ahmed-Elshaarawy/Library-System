from Library import library
from User import *
# regular = Regular()
credit = CreditCard()
class municipial_library(library):
    def __int__(self, allowed_list_of_user_types,  registered_users, restricted_users,
                books_in_library, borrowing_policy,  active_bookloans):
        self.location = "giza"
        super(municipial_library, self).__int__(allowed_list_of_user_types,  registered_users, restricted_users,
                books_in_library, borrowing_policy,  active_bookloans)

    def add_user(self, user):
        if user.address == self.location:
            self.registerd_user.append(user)
            print("your municipal matches the library municipality requirements, The user added successfully")
        else:
            print("The user can't be added because the municipal doesn't matches the library municipality requirements")

    def borrowBook(self, book: Book):
        if credit.available_credit >= 20:
             print("you can borrow a book")
             borrow_book = self.borrowedBooks.append(book)
        else:
            print("you should have credit balance in your credit card")
