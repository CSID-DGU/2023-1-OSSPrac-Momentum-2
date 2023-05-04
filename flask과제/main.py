from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    student_number = request.form['student_number']
    major = request.form['major']
    email_id = request.form['email_id']
    email_addr = request.form['email_addr']
    gender = request.form['gender']
    return render_template('result.html', name=name, student_number=student_number, major=major, email_id=email_id, email_addr=email_addr, gender=gender)

if __name__=='__main__':
    app.run(debug=True)