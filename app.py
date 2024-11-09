from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Función para conectar a la base de datos
def db_connection():
    conn = sqlite3.connect('alumnos.db')
    conn.row_factory = sqlite3.Row
    return conn

# Ruta de inicio – Lista de estudiantes
@app.route('/')
def home():
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM alumnos")
    students = cur.fetchall()
    conn.close()
    return render_template('home.html', students=students)

# Ruta para ver detalles de un estudiante
@app.route('/students/<int:student_id>')
def student_detail(student_id):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM alumnos WHERE id=?", (student_id,))
    student = cur.fetchone()
    conn.close()
    if student:
        return render_template('post/edit.html', student=student)
    return "Estudiante no encontrado", 404

# Ruta para crear un nuevo estudiante
@app.route('/students/create', methods=['GET', 'POST'])
def create_student():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        aprobado = bool(request.form['aprobado'])
        nota = float(request.form['nota'])
        fecha = request.form['fecha']

        conn = db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO alumnos (nombre, apellido, aprobado, nota, fecha)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, apellido, aprobado, nota, fecha))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))

    return render_template('post/create.html')

# Ruta para editar un estudiante
@app.route('/students/<int:student_id>/edit', methods=['GET', 'POST'])
def edit_student(student_id):
    conn = db_connection()
    cur = conn.cursor()
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        aprobado = bool(request.form['aprobado'])
        nota = float(request.form['nota'])
        fecha = request.form['fecha']

        cur.execute("""
            UPDATE alumnos
            SET nombre = ?, apellido = ?, aprobado = ?, nota = ?, fecha = ?
            WHERE id = ?
        """, (nombre, apellido, aprobado, nota, fecha, student_id))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))

    cur.execute("SELECT * FROM alumnos WHERE id=?", (student_id,))
    student = cur.fetchone()
    conn.close()
    if student:
        return render_template('post/edit.html', student=student)
    return "Estudiante no encontrado", 404


# Ruta para eliminar un estudiante
@app.route('/students/<int:student_id>/delete', methods=['POST'])
def delete_student(student_id):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM alumnos WHERE id=?", (student_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

