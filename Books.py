class Book:
    def __init__(self, title, authors, ISBN, noOfCps=1, noOfCpsBorrowed=0, physOrOnline=0, loanPeriod=30,
                 borrowers=list()):
        self._title = title
        self._authors = authors
        self._ISBN = ISBN
        self._noOfCps = noOfCps
        self._noOfCpsBorrowed = noOfCpsBorrowed
        self._physOrOnline = physOrOnline
        self._loanPeriod = loanPeriod
        self._borrowers = borrowers

    # getters
    @property
    def title(self):
        return self._title

    @property
    def authors(self):
        return self._authors

    @property
    def ISBN(self):
        return self._ISBN

    @property
    def noOfCps(self):
        return self._noOfCps

    @property
    def noOfCpsBorrowed(self):
        return self._noOfCpsBorrowed

    @property
    def physOrOnline(self):
        return self._physOrOnline

    @property
    def loanPeriod(self):
        return self._loanPeriod

    @property
    def borrowers(self):
        return self._borrowers

    # setters
    @title.setter
    def title(self, title):
        self._title = title

    @authors.setter
    def authors(self, authors):
        self._authors = authors

    @ISBN.setter
    def ISBN(self, ISBN):
        self._ISBN = ISBN

    @noOfCps.setter
    def noOfCps(self, noOfCps):
        self._noOfCps = noOfCps

    @noOfCpsBorrowed.setter
    def noOfCpsBorrowed(self, noOfCpsBorrowed):
        self._noOfCpsBorrowed = noOfCpsBorrowed

    @physOrOnline.setter
    def physOrOnline(self, physOrOnline):
        self._physOrOnline = physOrOnline

    @loanPeriod.setter
    def loanPeriod(self, loanPeriod):
        self._loanPeriod = loanPeriod

    @borrowers.setter
    def borrowers(self, borrowers):
        self._borrowers = borrowers

    def __eq__(self, other):
        if isinstance(other, type(self)):
            if self.ISBN == other.ISBN:
                return True
            elif (self.title == other.title) and (self.authors == other.authors):
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
        return f'Book Details are:\n' \
               f'Title: {self.title}\n' \
               f'Authors: {self.authors}\n' \
               f'ISBN: {self.ISBN}\n' \
               f'Total number of copies: {self.noOfCps}\n' \
               f'{"This book is available as a hard copy only" if (self.physOrOnline == 0) else None}' \
               f'{"This book is available as an online copy only" if (self.physOrOnline == 1) else None}' \
               f'{"This book is available as a hard copy as well as online" if (self.physOrOnline == 2) else None}' \
               f'\nLoan duration for this book is: {self.loanPeriod}\n' \
               f'Currently the following patrons are borrowing the book:{self.borrowers}\n'
