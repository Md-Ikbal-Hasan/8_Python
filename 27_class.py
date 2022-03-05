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

    # object method........
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



#instance/object
book_1 = ProgrammingBook('C Programming' , 180, 'Subeen'  ,1982,286)
book_2 = ProgrammingBook('C++ programming', 250 , 'Anisul' , 1985,120)
book_3 = ProgrammingBook('Programming for All', 190 , 'Tamim' , 1989,345)

""" 
book_3.name  ="Python Programming"

print(book_1.name , book_1.price)
print(book_2.name, book_2.price)
print(book_3.name)
print(book_1.publisher_name)
print(book_2.publisher_name)
"""




""" 
book_1.get_book_info()
book_1.author_info()
print("No of Books/object : ",ProgrammingBook.no_of_books)

print(f'Book 1 price {book_1.price}')
book_1.apply_discount()
print(f'Book 1 price after discount {book_1.price}')


print(f'Book 2 price {book_2.price}')
book_2.discount = 0.6
book_2.apply_discount()
print(f'Book 2 price after discount {book_2.price}')

print(book_1.price)
print(book_1.discount)
ProgrammingBook.set_discount(0.7)
print(book_1.discount)
book_1.apply_discount()
print(book_1.price)



book_str = "harry potter , 200 , JK Rowling  ,1970 , 400"
harry_potter = ProgrammingBook.constructor_from_string(book_str)
print(harry_potter.name)
"""



book_1.get_book_info()
ProgrammingBook.is_large_book(book_1.no_of_pages)

book_2.get_book_info()
ProgrammingBook.is_large_book(book_2.no_of_pages)



