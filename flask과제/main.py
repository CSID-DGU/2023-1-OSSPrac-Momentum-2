from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    student_number = request.form['student_number']
    major = request.form['major']
    return render_template('result.html', name=name, student_number=student_number, major=major)

if __name__=='__main__':
    app.run()