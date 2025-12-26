import mysql.connector as mysql

db = mysql.connect(
    username='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()
cursor.execute(
    """
    INSERT INTO students (name, second_name)
    VALUES (%s, %s)
    """,
    ("Petr", "Petrov")
)
db.commit()

student_id = cursor.lastrowid
print(f"Add student, id = {student_id}")

books = [
    "Python projekte",
    "Powerful Python",
    "Der Weg zum Python-Profi"
]

books_data = [(title, student_id) for title in books]

cursor.executemany(
    """
    INSERT INTO books (title, taken_by_student_id)
    VALUES (%s, %s)
    """,
    books_data
)

db.commit()
print("Books added")


cursor.execute(
    """
    INSERT INTO `groups` (title, start_date, end_date)
    VALUES (%s, %s, %s)
    """,
    ("Auto tester", "2025-10-01", "2026-02-01")
)
db.commit()

group_id = cursor.lastrowid
print(f"Add group, id = {group_id}")

cursor.execute(
    """
    UPDATE students
    SET group_id = %s
    WHERE id = %s
    """,
    (group_id, student_id)
)
db.commit()

print("Student added to the group")

subjects = ["Programming", "Technology"]
subject_ids = {}

for subject in subjects:
    cursor.execute(
        """
        INSERT INTO subjects (title)
        VALUES (%s)
        """,
        (subject,)
    )
    subject_ids[subject] = cursor.lastrowid

db.commit()
print(f"Add subjects: {subject_ids}")

lessons = [
    ("Proga 1", subject_ids["Programming"]),
    ("Proga 2", subject_ids["Programming"]),
    ("Tech 1", subject_ids["Technology"]),
    ("Tech 2", subject_ids["Technology"]),
]

lesson_ids = []

for title, subject_id in lessons:
    cursor.execute(
        """
        INSERT INTO lessons (title, subject_id)
        VALUES (%s, %s)
        """,
        (title, subject_id)
    )
    lesson_ids.append(cursor.lastrowid)

db.commit()
print(f"Add lessons, id = {lesson_ids}")

marks_data = [(5, lesson_id, student_id) for lesson_id in lesson_ids]

cursor.executemany(
    """
    INSERT INTO marks (value, lesson_id, student_id)
    VALUES (%s, %s, %s)
    """,
    marks_data
)

db.commit()
print("Student marks are set")

cursor.execute(
    """
    SELECT m.value, l.title
    FROM marks m
    JOIN lessons l ON m.lesson_id = l.id
    WHERE m.student_id = %s
    """,
    (student_id,)
)

marks = cursor.fetchall()
print("\nStudent's marks:")
for value, lesson in marks:
    print(f"{lesson}: {value}")

cursor.execute(
    """
    SELECT title
    FROM books
    WHERE taken_by_student_id = %s
    """,
    (student_id,)
)

books = cursor.fetchall()
print("\nStudent's books:")
for (title,) in books:
    print(title)

cursor.execute(
    """
    SELECT
        s.id,
        s.name,
        s.second_name,
        g.title AS group_title,
        GROUP_CONCAT(DISTINCT b.title SEPARATOR ', ') AS books,
        GROUP_CONCAT(
            DISTINCT CONCAT(l.title, ' (', sub.title, ') — ', m.value)
            SEPARATOR '; '
        ) AS lessons_with_marks
    FROM students s
    LEFT JOIN `groups` g ON s.group_id = g.id
    LEFT JOIN books b ON b.taken_by_student_id = s.id
    LEFT JOIN marks m ON m.student_id = s.id
    LEFT JOIN lessons l ON m.lesson_id = l.id
    LEFT JOIN subjects sub ON l.subject_id = sub.id
    WHERE s.id = %s
    GROUP BY s.id
    """,
    (student_id,)
)

student_card = cursor.fetchone()

print("\nStudent's card:")
print(f"ID: {student_card[0]}")
print(f"Name: {student_card[1]} {student_card[2]}")
print(f"Group: {student_card[3]}")
print(f"Books: {student_card[4]}")
print(f"Lessons and marks: {student_card[5]}")

cursor.close()
db.close()
