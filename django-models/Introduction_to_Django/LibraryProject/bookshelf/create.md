# Create Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
```

## Output
```
<Book: 1984>
```

## Description
Successfully created a Book instance with title "1984", author "George Orwell", and publication year 1949.