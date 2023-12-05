
# run.py
from flask import Flask
from app.controllers.book_controller import book_bp  # Importa o Blueprint do diretório 'app.controllers'

app = Flask(__name__)

# Registrando o Blueprint no aplicativo Flask
app.register_blueprint(book_bp)

if __name__ == '__main__':
    app.run()
