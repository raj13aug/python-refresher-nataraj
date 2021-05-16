#Inheritance means that a book is a bookshelf,
# composition means that a bookshelf has many books

class Bookshelf:
  def __init__(self, *books):
    self.books = books
	
  def __str__(self):
    return f"Bookshelf with {len(self.books)} books"
		
class Book:
  def __init__(self,name):
    self.name = name
	 
  def __str__(self):
    return f"Book {self.name}"
		

book = Book("Harry Potter")
book2 = Book("python 101")
shelf = Bookshelf(book, book2)

print(shelf)
