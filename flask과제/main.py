from flask import Flask, redirect, render_template, request

app = Flask(__name__)

result_list=[]

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/delete', methods=['POST'])
def delete():
    global result_list
    delete_idx = int(request.form.get('delete'))
    del result_list[delete_idx]
    return render_template('result.html', result=result_list)

@app.route('/result', methods=['POST','GET'])
def result():

    global result_list
    if request.method=='POST':
        result=dict()
        result['Name'] = request.form.get('name')
        result['StudentNumber'] = request.form.get('student_number')
        result['major'] = request.form.get('major')
        result['email'] = request.form.get('email') +'@'+ request.form.get('email_addr')
        result['gender'] = request.form.get('gender')
        result['Languages'] = ','.join(request.form.getlist('language'))
        result_list.append(result)
        result_list.sort(key=lambda x: x['StudentNumber'])
        return render_template('result.html', result=result_list)

if __name__=='__main__':
    app.run(debug=True, port=8002)