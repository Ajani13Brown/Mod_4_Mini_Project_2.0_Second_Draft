class Book():
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

    def book_info(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Genre: {self.genre}')
