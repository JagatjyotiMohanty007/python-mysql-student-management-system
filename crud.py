from db_connection import get_connection

def insert_student(name, age, city):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO students(name, age, city)
    VALUES(%s,%s,%s)
    """

    cursor.execute(query, (name, age, city))
    conn.commit()

    cursor.close()
    conn.close()

def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()

def update_student(student_id, city):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE students
    SET city=%s
    WHERE id=%s
    """

    cursor.execute(query, (city, student_id))
    conn.commit()

    cursor.close()
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM students WHERE id=%s"

    cursor.execute(query, (student_id,))
    conn.commit()

    cursor.close()
    conn.close()
