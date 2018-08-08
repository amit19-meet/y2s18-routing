from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/student/<int:student_id>')
def display_student(student_id, name, year, finished_lab):
    return render_template('student.html', student_id=query_by_id(student_id), student.name= "Amit", student.year= "Y2", student.finished_lab= True )

app.run(debug=True)
