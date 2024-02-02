#Exercise 6 : librory Management 
class librory:
    def __init__(self):
        self.nobooks=0
        self.books=[]
    def addbook(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)
    def show_books(self):
        for book in self.books:
            print(book)
        print(f" number of books are :{self.nobooks}")
l1=librory()
l1.addbook("the history")
l1.addbook("the secret")
l1.addbook("the ramayana")
l1.show_books()
string="indian_ancient"
l2=librory()
l2.addbook("Ayurved_the_indian_ancient_book")
l2.addbook("Bhagvad_puran")
l2.show_books()
print(l2.books)

















