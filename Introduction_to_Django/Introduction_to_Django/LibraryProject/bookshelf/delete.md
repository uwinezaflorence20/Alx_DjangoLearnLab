# Delete Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
books = Book.objects.all()
print(f"All books: {books}")
```

## Output
```
(1, {'bookshelf.Book': 1})
All books: <QuerySet []>
```

## Description
Successfully deleted the Book instance. Confirmed deletion by querying all books, which returned an empty QuerySet.