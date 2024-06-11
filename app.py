from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = postgresql://username:password@localhost:5432/bookdb

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1024), nullable=False)
    author = db.Column(db.String(1024), nullable=False)
    description = db.Column(db.String(5012), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        description = request.form['description']
        new_book = Book(title=title, author=author, description=description)
        try:
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return 'There was an issue adding your book'
    
    books = Book.query.all()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
