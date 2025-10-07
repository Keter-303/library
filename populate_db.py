import os
import django
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'library'))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")
django.setup()

from api.models import Author, Publisher, Book

def populate_database():
   
    knuth, _ = Author.objects.get_or_create(name="Donald Knuth")
    tanenbaum, _ = Author.objects.get_or_create(name="Andrew S. Tanenbaum")
    cormen, _ = Author.objects.get_or_create(name="Thomas H. Cormen")
    petzold, _ = Author.objects.get_or_create(name="Charles Petzold")
    fowler, _ = Author.objects.get_or_create(name="Martin Fowler")
    go4, _ = Author.objects.get_or_create(name="Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides")

    print("Authors created.")

   
    addison_wesley, _ = Publisher.objects.get_or_create(name="Addison-Wesley Professional")
    prentice_hall, _ = Publisher.objects.get_or_create(name="Prentice Hall")
    mit_press, _ = Publisher.objects.get_or_create(name="MIT Press")
    microsoft_press, _ = Publisher.objects.get_or_create(name="Microsoft Press")
    oreilly, _ = Publisher.objects.get_or_create(name="O'Reilly Media")

    print("Publishers created.")


    Book.objects.get_or_create(
        title="The Art of Computer Programming",
        author=knuth,
        publisher=addison_wesley,
        defaults={
            "description":"A comprehensive monography written by Donald Knuth that covers many kinds of programming algorithms and their analysis.",
            "genre":"Algorithms",
            "price":85.50,
            "popularity": 95
        }
    )

    Book.objects.get_or_create(
        title="Computer Networks",
        author=tanenbaum,
        publisher=prentice_hall,
        defaults={
            "description":"A classic textbook on computer networking.",
            "genre":"Networking",
            "price":65.00,
            "popularity": 88
        }
    )

    Book.objects.get_or_create(
        title="Introduction to Algorithms",
        author=cormen,
        publisher=mit_press,
        defaults={
            "description":"A comprehensive textbook on computer algorithms.",
            "genre":"Algorithms",
            "price":92.75,
            "popularity": 98
        }
    )

    Book.objects.get_or_create(
        title="Code: The Hidden Language of Computer Hardware and Software",
        author=petzold,
        publisher=microsoft_press,
        defaults={
            "description":"Explains the inner workings of computers.",
            "genre":"Computer Architecture",
            "price":35.20,
            "popularity": 90
        }
    )

    Book.objects.get_or_create(
        title="Refactoring: Improving the Design of Existing Code",
        author=fowler,
        publisher=addison_wesley,
        defaults={
            "description":"A book on software refactoring.",
            "genre":"Software Engineering",
            "price":55.00,
            "popularity": 85
        }
    )
    
    Book.objects.get_or_create(
        title="Design Patterns: Elements of Reusable Object-Oriented Software",
        author=go4,
        publisher=addison_wesley,
        defaults={
            "description":"A classic book that introduces design patterns in software engineering.",
            "genre":"Software Engineering",
            "price":60.00,
            "popularity": 92
        }
    )

    print("Books created.")
    print("Database population complete!")

if __name__ == '__main__':
    populate_database()
