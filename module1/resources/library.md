
### Exercise: Library Management System

**Scenario:**
You are tasked with developing a simple library management system to keep track of books and their availability.

**Requirements:**
1. Create a `Book` class with the following attributes:
   - `title` (string)
   - `author` (string)
   - `isbn` (string or integer)
   - `available` (boolean indicating if the book is available or not)

2. Create a `Library` class that manages a collection of `Book` objects. It should have the following methods:
   - `add_book(title, author, isbn)`: Adds a new `Book` to the library. Initially, set the book as available.
   - `remove_book(isbn)`: Removes the book with the given ISBN from the library.
   - `find_book(title)`: Returns a list of `Book` objects that match the given title.
   - `list_available_books()`: Prints a list of all available books in the library.

**Instructions:**
- Implement the `Book` class first, ensuring it can represent a book with the specified attributes.
- Then implement the `Library` class, ensuring each method works correctly based on its description.
