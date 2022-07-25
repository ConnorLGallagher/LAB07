from flask import Flask, render_template, session, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
app = Flask (__name__)

app.config['SECRET_KEY']='oursecretkey'

class MyForm(FlaskForm):
    username=StringField('Enter Username:')
    password=StringField('Enter Password:')
    submit=SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
    form= MyForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        session['password'] = form.password.data
        return redirect(url_for('report'))
    return render_template('index.html', form=form)
@app.route('/report')
def report():
    pword=request.args.get('password')
    return render_template('report.html',pword=pword)

if __name__ == '__main__':
    app.run(debug=True)