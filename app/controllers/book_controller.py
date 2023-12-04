# controllers/book_controller.py

from flask import Blueprint, jsonify
from app.services.book_service import BookService

book_bp = Blueprint('book', __name__, url_prefix='/books')
book_service = BookService()

@book_bp.route('/', methods=['GET'])
def get_all_books():
    books = book_service.get_all_books()
    # Converte os objetos Book para um formato serializável (por exemplo, dict) antes de retornar como JSON
    serialized_books = [book.__dict__ for book in books]
    return jsonify(serialized_books)

@book_bp.route('/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = book_service.get_book_by_id(book_id)
    # Converte o objeto Book para um formato serializável antes de retornar como JSON
    serialized_book = book.__dict__
    return jsonify(serialized_book)
