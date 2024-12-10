from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, RadioField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TwojTajnyKlucz'


class MyForm(FlaskForm):
    name = StringField('Imię', validators=[DataRequired()])
    birthdate = DateField('Data urodzenia',  format='%Y-%m-%d', validators=[DataRequired()])
    profession = SelectField('Zawód', choices=[
        ('programista', 'Programista'),
        ('nauczyciel', 'Nauczyciel'),
        ('lekarka', 'Lekarz'),
        ('inżynier', 'Inżynier'),
        ('artysta', 'Artysta')
        ], validators=[DataRequired()])
    student_status = RadioField('Status studenta', choices=[
        ('tak', 'Tak'),
        ('nie', 'Nie')
        ], validators=[DataRequired()])
    location = StringField('Miejsce zamieszkania', validators=[DataRequired()])
    submit = SubmitField('Wyślij')


@app.route('/')
def hello():
    return 'Witaj na mojej stronie'

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        flash(f'Imię i nazwisko: {form.name.data}, Data urodzenia: {form.birthdate.data}, Zawód: {form.profession.data}, Status studenta: {form.student_status.data}, Miejsce zamieszkania: {form.location.data}', 'success')
        return redirect(url_for('form'))  
    return render_template('form2.html', form=form)




# @app.route('/form', methods=['GET'])
# def form():
#     return render_template('form.html', form=form)


# @app.route('/submit', methods=['POST'])
# def loading_data():

#     name = request.form.get('name')
#     birthdate = request.form.get('birthdate')
#     profession = request.form.get('profession')
#     student_status = request.form.get('student_status')
#     location = request.form.get('location')
#     return render_template('form_table.html', name=name, birthdate=birthdate, profession=profession, student_status=student_status, location=location)


if __name__=="__main__":
    with app.app_context():
        app.run(debug=True)