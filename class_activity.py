# Define the Book class
class Book:
  def __init__(self, title, author, year, checked_out=False):
    self.title = title
    self.author = author
    self.year = year
    self.checked_out = checked_out

  def display_info(self):
    if self.checked_out:
      status = "Checked Out"
    else:
      status = "Available"

    print(f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nStatus: {status}\n")


  def check_out(self):
    if not self.checked_out:
      self.checked_out = True
      print(f"'{self.title}' has been checked out")
    else:
      print(f"'{self.title}' is already checked out")

  def return_book(self):
    if self.checked_out:
      self.checked_out = False
      print(f"'{self.title}' has been returned and is now available")
    else:
      print(f"'{self.title}' was not checked out")

            
book1 = Book("xyz", "abc", 2000, True)
book2 = Book("book2", "author2", 2025, False)

# Display details
book1.display_info()
book2.display_info()

# Check out and return
book1.check_out()
book1.display_info()

book1.return_book()
book1.display_info()
