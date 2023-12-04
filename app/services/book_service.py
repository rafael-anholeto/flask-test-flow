# services/book_service.py

from app.repositories.book_repository import BookRepository

class BookService:
    def __init__(self):
        self.book_repository = BookRepository()

    def get_books():
        return BookRepository.get_books()

    def get_books_by_id(book_id):
        return BookRepository.get_books_by_id(book_id)
    
    def create_book():
        return BookRepository.create_book()
    
    
    def update_book( book_id):
        return BookRepository.update_book(book_id)
    
    
    def delete_book(book_id):
        return BookRepository.delete_book(book_id)


