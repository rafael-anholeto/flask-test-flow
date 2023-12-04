from flask import Flask, request, jsonify, abort, make_response
from datetime import datetime
from app.models import Book


app = Flask(__name__)



books = [
    Book(id=1, title='The Hobbit', timestamp= datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
    Book(id=2, title='Lord of the Rings', timestamp= datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
]

@app.route('/books', methods=['GET'])
def get_books():
    # Serializa a lista de livros em um formato JSON
    serialized_books = [book.serialize() for book in books]
    return jsonify(serialized_books)


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book.id == book_id:  # Comparando o atributo id do objeto Book
            return jsonify(book.serialize())

    response = make_response('Livro não encontrado', 404)
    return response
    
    
# Create
@app.route('/books', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
        
    book = Book(
        id=books[-1].id + 1 if books else 1,
        title = request.json['title'],
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
    
    books.append(book)
    return jsonify(book.serialize()), 201 

# Update

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = [book for book in books if book.id == book_id]

    if len(book) == 0:
        abort(404)

    if not request.json:
        abort(400)

    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)

    if 'available' in request.json and type(request.json['available']) is not bool:
        abort(400)

    book[0].title = request.json.get('title', book[0].title)
    book[0].timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return jsonify(book[0].serialize())


# Delete
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = [book for book in books if book.id == book_id]
    
    if len(book) == 0:
        abort(404)
        
    books.remove(book[0])
    
    return jsonify({'result': True})





# # run.py

# from flask import Flask
# # from app.config.config import DevelopmentConfig
# from app.controllers.book_controller import book_bp

# app = Flask(__name__)
# # app.config.from_object(DevelopmentConfig)

# app.register_blueprint(book_bp)

# if __name__ == '__main__':
#     app.run()




from flask import Flask, request, jsonify, abort, make_response


app = Flask(__name__)

if __name__ == '__main__':
    app.run()