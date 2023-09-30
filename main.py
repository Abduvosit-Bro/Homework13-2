import sqlite3

conn = sqlite3.connect('students.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE students 
          (id INTEGER PRIMARY KEY, 
           name TEXT,
           age INTEGER,
           grade TEXT)
          ''')

c.execute("INSERT INTO students VALUES (1, 'John Wick', 18, 'A')")
c.execute("INSERT INTO students VALUES (2, 'The Rock', 19, 'B')")
c.execute("INSERT INTO students VALUES (3, 'Andrew Tate', 20, 'C')")


def get_student_by_name(name):
    c.execute("SELECT * FROM students WHERE name=?", (name,))
    return c.fetchone()


def update_student_grade(name, new_grade):
    c.execute("UPDATE students SET grade=? WHERE name=?", (new_grade, name))
    conn.commit()


def delete_student(name):
    c.execute("DELETE FROM students WHERE name=?", (name,))
    conn.commit()


conn.close()
