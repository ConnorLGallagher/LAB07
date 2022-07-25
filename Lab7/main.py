from flask import Flask, render_template, session, redirect, url_for, request
app = Flask (__name__)

app.config['SECRET_KEY']='oursecretkey'
def checkUpper(pword):
    result=False
    for i in pword:
        if i.isupper():
            result = True
            break
    return result
def checkLower(pword):
    result=False
    for i in pword:
        if i.islower():
            result = True
            break
    return result
def checkLength(pword):
    num=0
    for i in pword:
        num+=1
    if num>8:
        result=True
    else:
        result=False
    return result
def checkNum(pword):
    return (pword[-1].isdigit())
@app.route('/')
def index():
    return render_template('index.html',)
@app.route('/report')
def report():
    password=request.args.get('password')
    badlen= checkLength(password)
    badup= checkUpper(password)
    badlow= checkLower(password)
    badnum= checkNum(password)
    return render_template('report.html',badlen=badlen,badup=badup,badlow=badlow,badnum=badnum)

if __name__ == '__main__':
    app.run(debug=True)