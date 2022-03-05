class ProgrammingBook:
    no_of_books = 0  # class variable

    discount = 0.5

    def __init__(self,name,price, author_name, author_born,no_of_pages):
        self.name = name
        self.price= price
        self.author_name = author_name
        self.author_born = author_born
        self.no_of_pages = no_of_pages
        self.publisher_name = "Coding_lover" # this is fixed for all object
        ProgrammingBook.no_of_books += 1

    # regular method........
    def get_book_info(self):
        print(f"Book name: {self.name} , Price: {self.price} ,Page: {self.no_of_pages}")

    def author_info(self):
        print(f"Author Name: {self.author_name} , Author Born: {self.author_born}")

    def apply_discount(self):
        self.price = int(self.price - self.price * self.discount)

    # class method........
    @classmethod
    def set_discount(cls,new_discount):
        cls.discount = new_discount

    @classmethod
    def constructor_from_string(cls,book_str):
        name ,price , author_name , author_born , pages = book_str.split(',')
        return cls(name ,price , author_name , author_born , pages)

    #static mehod
    @staticmethod
    def is_large_book(page):

        if int(page) > 200:
            print("yes it is a large book ! ")
        elif int(page)<=200:
            print("No it is not a large Book")



class Library:
    def __init__(self,book_list = None):
        if book_list is None:
            self.book_list = []
        else:
            self.book_list = book_list

    def get_all_books(self):
        for book in self.book_list:
            print(f"Title: {book.name} , Author: {book.author_name} ,Price: {book.price}")

    def add_book(self,book):
        self.book_list.append(book)

    def remove_book(self,book):
        self.book_list.remove(book)






#instance/object
book_1 = ProgrammingBook('C Programming' , 180, 'Subeen'  ,1982,286)
book_2 = ProgrammingBook('C++ programming', 250 , 'Anisul' , 1985,120)
book_3 = ProgrammingBook('Programming for All', 190 , 'Tamim' , 1989,345)

public_library  = Library()

public_library.add_book(book_1)
public_library.add_book(book_2)

public_library.get_all_books()
public_library.remove_book(book_1)
print("after delete : ")
public_library.get_all_books()




