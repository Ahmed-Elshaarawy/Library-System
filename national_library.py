from User import *
from Library import *
credit = CreditCard

class national_Library:
    def __int__(self, allowed_list_of_user_types,  registered_users, restricted_users,
                books_in_library, borrowing_policy,  active_bookloans):

        super(national_Library, self).__int__(allowed_list_of_user_types,  registered_users, restricted_users,
                books_in_library, borrowing_policy,  active_bookloans)

    def add_user(self,s, a, user):
        if isinstance(user, Regular):
            if Regular.social_number == s and Regular.age == a:
                self.registered_user.append(user)
                print("User have been added ")
        else:
            print("User can't be added")

    def borrowBook(self, book: Book):
        if credit.available_credit >= 20:
             print("you can borrow a book")
             borrow_book = self.borrowedBooks.append(book)
        else:
            print("you should have credit balance in your credit card")
