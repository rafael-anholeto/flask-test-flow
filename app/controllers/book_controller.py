# app/controllers/book_controller.py
from flask import Blueprint
from app.services.book_service import BookService  # Importa o serviço do diretório 'app.services'

book_bp = Blueprint('book', __name__, url_prefix='/books')

@book_bp.route('', methods=['GET'])
def get_books():
    # Implementação para obter livros
    return BookService.get_books()

@book_bp.route('/<int:book_id>', methods=['GET'])
def get_books_by_id(book_id):
    # Implementação para obter informações sobre um livro específico
    return BookService.get_books_by_id(book_id)

@book_bp.route('', methods=['POST'])
def create_book():
    # Implementação para criar um livro
    return BookService.create_book()


@book_bp.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    # Implementação para atualizar um livro
    return BookService.update_book(book_id)

@book_bp.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    # Implementação para deletar um livro
    return BookService.delete_book(book_id)