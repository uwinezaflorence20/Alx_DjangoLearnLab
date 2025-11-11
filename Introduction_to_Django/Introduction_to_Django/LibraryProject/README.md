# LibraryProject

A Django-based library management system.

## Description
This project is part of the ALX Django Learning Lab. It demonstrates the setup and configuration of a Django project.

## Installation
1. Install Django: `pip install django`
2. Run migrations: `python manage.py migrate`
3. Start the server: `python manage.py runserver`

## Project Structure
- `manage.py`: Django's command-line utility
- `LibraryProject/settings.py`: Project configuration
- `LibraryProject/urls.py`: URL routing configuration
```

### 2. **Verify File Structure**
The checker expects this exact structure:
```
Alx_DjangoLearnLab/
└── Introduction_to_Django/
    └── LibraryProject/
        ├── README.md          ← Must exist and have content
        ├── manage.py          ← Must exist
        └── LibraryProject/
            ├── __init__.py
            ├── settings.py    ← Must exist with correct content
            ├── urls.py
            ├── asgi.py
            └── wsgi.py



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