from flask import Flask, redirect, render_template, request

app = Flask(__name__)

result_list=[]

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/delete', methods=['POST'])
def delete():
    global result_list
    if request.form.get('action') == 'delete':
        to_delete = request.form.getlist('delete[]')
        for idx in to_delete:
            del result_list[int(idx)]
        return render_template('result.html', result=result_list)

@app.route('/result', methods=['POST','GET'])
def result():

    global result_list
    if request.method=='POST':
        result=dict()
        result['이름'] = request.form.get('name')
        result['학번'] = request.form.get('student_number')
        result['전공'] = request.form.get('major')
        result['이메일'] = request.form.get('email') +'@'+ request.form.get('email_addr')
        result['성별'] = request.form.get('gender')
        result['프로그래밍 언어'] = ','.join(request.form.getlist('language'))
        if (result['이름'] == "" or result['학번'] == "" or result['전공'] == "" or result['이메일'] == "@"):
            return '<script>alert("필수 정보를 모두 입력해주세요!"); window.history.back();</script>'
        
        result_list.append(result)
        result_list.sort(key=lambda x: x['학번'])
        return redirect('/result')
    
    return render_template('result.html', result=result_list)

if __name__=='__main__':
    app.run(debug=True, port=8002)