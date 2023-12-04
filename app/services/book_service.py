# services/book_service.py

from app.repositories.book_repository import BookRepository

class BookService:
    def __init__(self):
        self.book_repository = BookRepository()

    def get_books(self):
        return self.book_repository.get_all_books()

    def get_book(self, book_id):
        return self.book_repository.get_book_by_id(book_id)
    
    def create_book(self):
        return self.book_repository.create_book()
    
    
    def update_book(self, book_id):
        return self.book_repository.update_book(book_id)
    
    
    def delete_book(self, book_id):
        return self.book_repository.delete_book(book_id)


