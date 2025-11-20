class Book:
    material = "бумага"
    has_text = True

    def __init__(self, title, author, pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def info(self):
        base = (
            f"Название: {self.title}, Автор: {self.author}, "
            f"страниц: {self.pages}, материал: {self.material}"
        )
        if self.reserved:
            print(base + ", зарезервирована")
        return base


class SchoolBook(Book):
    def __init__(self, title, author, pages, isbn, subject, grade, has_tasks=False, reserved=False):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.has_tasks = has_tasks

    def info(self):
        base = (
            f"Название: {self.title}, Автор: {self.author}, "
            f"страниц: {self.pages}, предмет: {self.subject}, класс: {self.grade}"
        )
        if self.reserved:
            print(base + ", зарезервирована")
        return base


book1 = SchoolBook("Алгебра", "Иванов", 200, "978-5-389-07477-1", "Математика", 9, has_tasks=True)
book2 = SchoolBook("Геометрия", "Петров", 180, "978-5-389-07477-2", "Математика", 7, has_tasks=False)
book3 = SchoolBook("История", "Сидоров", 320, "978-5-389-07477-3", "История", 6, has_tasks=True)
book4 = SchoolBook("География", "Андреев", 280, "978-5-389-07477-4", "География", 8, has_tasks=False)
book5 = SchoolBook("Биология", "Кузнецов", 220, "978-5-389-07477-5", "Биология", 10, has_tasks=True)

book3.reserved = True

for b in (book1, book2, book3, book4, book5):
    print(b.info())
