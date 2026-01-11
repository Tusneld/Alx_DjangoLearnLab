>>> from bookshelf.models import Book
>>> Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Expected Output: <Book: 1984>

>>> book = Book.objects.get(title="1984")
>>> print(book.title, book.author, book.publication_year)
# Expected Output: 1984 George Orwell 1949

>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(book.title)
# Expected Output: Nineteen Eighty-Four

>>> book.delete()
>>> Book.objects.all()
# Expected Output: <QuerySet []>