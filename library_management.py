class Book:
    def __init__(self,book_id,title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.availability = "Available" 
    def __str__ (self):
        return f"BOOK ID: {self.book_id} TITLE: {self.title} AUTHOR: {self.author} GENRE: {self.genre} AVAILABILITY: {self.availability}"
class User:
    def __init__(self,user_id,name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []
    def __str__ (self):
        return f"User ID: {self.user_id}, Name: {self.name}, Borrowed Books: {', '.join([str(book) for book in self.borrowed_books])}"
class Library:
    def __init__(self):
        self.books = []
        self.users = []
    def add_book(self,book_id,title,author,genre):
        self.books.append(Book(book_id,title,author,genre))
    def add_user(self,user_id,name):
        self.users.append(User(user_id,name))
    def borrow_books(self,user_id,book_id):
        for user in self.users:
            if user.user_id == user_id:
                for book in self.books:
                    if book.book_id == book_id and book.availability == 'Available':
                        book.availability = 'Checked Out'
                        user.borrowed_books.append(book)
                        return f"Book {book_id} borrowed successfully!"
        return "Book not found or not available for borrowing."            
    def return_books(self,user_id,book_id):
        for user in self.users:
            if user.user_id == user_id:
                for book in self.books:
                    if book.book_id == book_id:
                        book.availability == 'Available'
                        user.borrowed_books.remove(book)
                        return f"Book {book_id} returned successfully!"
        return "Book not found or not available in user's borrowed list."  
    def search_books(self,search_criteria,search_term):
        results = []
        for book in self.books:
            if search_criteria == "title" and search_term.lower() in book.title.lower():
                results.append(book)
            elif search_criteria == "author" and search_term.lower() in book.title.lower():
                results.append(book)
            elif search_criteria == "genre" and search_term.lower() in book.title.lower():
                results.append(book)
        return results
    def view_all_books(self):
        return self.books
    def view_available_books(self):
        return [book for book in self.books if book.availability == "Available"]
    def view_checked_out_books(self):
        return [book for book in self.books if book.availability == "Checked Out"]
def main():
    library = Library()
    while True:
        print("Library Management System")
        print("1.Add Book")
        print("2.Add User")
        print("3.Borrow Book")
        print("4.Return Book")
        print("5.Search Book")
        print("6.View All Books")
        print("7.View Available Books")
        print("8.View Checked Out Books")
        print("9.Exit")
        choice = input("Enter Your Choice:")
        if choice == "1":
            book_id = input("Enter Book ID:")
            title = input("Enter Book Title:")
            author = input("Enter Book Author:")
            genre = input("Enter Book Genre:")
            library.add_book(book_id,title,author,genre)
            print("Book added successfully.")
        elif choice == "2":
            user_id = input("Enter User ID:")
            name = input("Enter User name:")
            library.add_user(user_id,name)
            print("User added successfully.")
        elif choice == "3":
            user_id = input("Enter User ID:")
            book_id = input("Enter Book ID:")
            print(library.borrow_books(user_id,book_id))
        elif choice == "4":
            user_id = input("Enter User ID:")
            book_id = input("Enter Book ID:")
            print(library.return_books(user_id,book_id))
        elif choice == "5":
            search_criteria = input("Enter search criteria (title, author, genre):")
            search_term = input("Enter Search Term:")
            results = library.search_books(search_criteria,search_term)
            if results:
                for book in results:
                    print(book)
            else:
                print("No Book Found")
        elif choice == "6":
             for book in library.view_all_books():
                 print(book)
        elif choice == "7":
             for book in library.view_available_books():
                 print(book)
        elif choice == "8":
             for book in library.view_checked_out_books():
                 print(book)
        elif choice == "9":
            print("Exiting the System. GoodBye!")
            break
        else:
            print("You enter invalid a choice.")
main()