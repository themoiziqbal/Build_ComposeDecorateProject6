# Class methods
from random import randint

# The class keeps track of how many books have been created so far
class Book:
    count = 0
    @classmethod
    def increment_book_count(cls):
        cls.count += 1

    def __init__(self):
        Book.increment_book_count()

def main():
    # Create 10-15 books
    for i in range(0,randint(10,15)):
        Book()

    print(f"Books created: {Book.count}")
if __name__ == '__main__':
    main()
