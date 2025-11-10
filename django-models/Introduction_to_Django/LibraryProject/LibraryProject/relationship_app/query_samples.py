"""
Sample queries demonstrating Django ORM relationships.

To run these queries:
1. Navigate to: C:\Users\user\OneDrive\Desktop\Alx_DjangoLearnLab\django-models\Introduction_to_Django\LibraryProject
2. Run: python manage.py shell
3. Copy and paste the code from this file
"""

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    Demonstrates ForeignKey relationship usage.
    
    Args:
        author_name (str): The name of the author
    
    Returns:
        QuerySet: All books by the specified author
    """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None



def list_books_in_library(library_name):
    """
    List all books in a library.
    Demonstrates ManyToMany relationship usage.
    
    Args:
        library_name (str): The name of the library
    
    Returns:
        QuerySet: All books in the specified library
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None


def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    Demonstrates OneToOne relationship usage.
    
    Args:
        library_name (str): The name of the library
    
    Returns:
        Librarian: The librarian for the specified library
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")
        return None


def retrieve_librarian_alternative(library_name):
    """
    Alternative method: Query librarian directly.
    """
    try:
        librarian = Librarian.objects.get(library__name=library_name)
        
        print(f"\nLibrarian for {library_name} (alternative method):")
        print(f"  {librarian.name}")
        
        return librarian
    except Librarian.DoesNotExist:
        print(f"No librarian found for library '{library_name}'.")
        return None


# Sample usage and testing
if __name__ == "__main__":
    print("=" * 50)
    print("Django ORM Relationship Query Samples")
    print("=" * 50)
    
    # Example 1: Query books by author
    print("\n### Example 1: ForeignKey Relationship ###")
    query_books_by_author("J.K. Rowling")
    
    # Example 2: List books in a library
    print("\n### Example 2: ManyToMany Relationship ###")
    list_books_in_library("City Central Library")
    
    # Example 3: Retrieve librarian for a library
    print("\n### Example 3: OneToOne Relationship ###")
    retrieve_librarian_for_library("City Central Library")
    
    print("\n" + "=" * 50)


# Additional helper function to create sample data
def create_sample_data():
    """
    Helper function to create sample data for testing.
    Run this once to populate your database with test data.
    """
    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")
    author3 = Author.objects.create(name="Jane Austen")
    
    # Create books
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)
    book4 = Book.objects.create(title="Animal Farm", author=author2)
    book5 = Book.objects.create(title="Pride and Prejudice", author=author3)
    
    # Create libraries
    library1 = Library.objects.create(name="City Central Library")
    library2 = Library.objects.create(name="University Library")
    
    # Add books to libraries (ManyToMany)
    library1.books.add(book1, book2, book3, book5)
    library2.books.add(book3, book4, book5)
    
    # Create librarians
    librarian1 = Librarian.objects.create(name="Alice Johnson", library=library1)
    librarian2 = Librarian.objects.create(name="Bob Smith", library=library2)
    
    print("Sample data created successfully!")
    print(f"Created {Author.objects.count()} authors")
    print(f"Created {Book.objects.count()} books")
    print(f"Created {Library.objects.count()} libraries")
    print(f"Created {Librarian.objects.count()} librarians")