from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

add_student("Amit", 2, False)
add_student("Noam", 2, True)
@app.route('/student/<int:student_id>')
def display_student(student_id, name= "name", year= "year", finished_lab= "finished_lab"):
    return render_template('student.html', student=query_by_id(student_id))

app.run(debug=True)
