# Django Admin Configuration for Book Model

## Admin Registration

The Book model has been registered with the Django admin interface with custom configurations.

## Configuration Details

### File: `bookshelf/admin.py`
```python
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)
```

## Features

### List Display
- Shows `title`, `author`, and `publication_year` as columns in the admin list view
- Provides a clear overview of all books at a glance

### List Filter
- Sidebar filter for `publication_year`
- Allows quick filtering of books by their publication year

### Search Functionality
- Search by `title` or `author`
- Enables quick lookup of specific books

## Accessing the Admin Interface

1. Create a superuser: `python manage.py createsuperuser`
2. Start the server: `python manage.py runserver`
3. Navigate to: `http://127.0.0.1:8000/admin/`
4. Log in with superuser credentials

## Usage

- **Add Books**: Click "Add Book" button
- **Edit Books**: Click on any book in the list
- **Delete Books**: Select books and choose delete action
- **Search**: Use the search box at the top
- **Filter**: Use the sidebar filter on the right