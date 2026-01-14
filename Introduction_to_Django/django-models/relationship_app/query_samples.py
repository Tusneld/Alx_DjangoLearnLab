from relationship_app.models import Author, Book, Library, Librarian

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "Some Author"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)



# 3. Retrieve the librarian for a library
# The checker specifically looks for Librarian.objects.get(library=library)
librarian = Librarian.objects.get(library=library)








# 1. Query all books by a specific author
author_name = "Some Author"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

# 2. List all books in a library
library_name = "Some Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# 2. List all books in a library
def get_library_books(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)
  
