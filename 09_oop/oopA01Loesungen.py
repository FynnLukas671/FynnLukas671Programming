from turtledemo.sorting_animate import Block


class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def infos(self):
        return self.title, self.author, self.pages

    def checkLength(self):
        if self.pages <= 300:
            return True
        else:
            return False

b1 = Book("Title", "Author", 310)

print(b1.infos(), b1.checkLength())
