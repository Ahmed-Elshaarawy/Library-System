def searchForBook(title, bookList):
    bookIndex = -1
    for i, book in enumerate(bookList):
        if book.title == title:
            bookIndex = i
    return bookIndex

def searchForUser(name, SchoolList):
    userIndex = -1
    for i, user in enumerate(SchoolList):
        if user[0] == name:
            userIndex = i
    return userIndex

def search_user(name, municipialList):
    userIndex = -1
    for i, user in enumerate(municipialList):
        if user[0] == name:
            userIndex = i
    return userIndex

def search_User(name, nationalList):
    userIndex = -1
    for i, user in enumerate(nationalList):
        if user[0] == name:
            userIndex = i
    return userIndex