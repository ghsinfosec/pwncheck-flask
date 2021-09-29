from flask import Flask, render_template, request, flash, redirect, url_for
from util import pwncheck, pw_generator
from forms import PasswordForm, PWGeneratorForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_KEY_HERE'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PasswordForm()
    password = form.password.data

    if form.validate_on_submit():
        status, message = pwncheck.pwncheck(password)
        if message == 'compromised':
            flash(status, 'danger')
            return render_template('index.html', form=form)
        elif message == 'safe':
            flash(status, 'success')
            return render_template('index.html', form=form)

    return render_template('index.html', form=form)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('generator', methods=['GET', 'POST'])
def generator():
    form = PWGeneratorForm()
    password = pw_generator.generate_pw()

    if form.validate_on_submit():
        return render_template('generator.html', form=form, password=password)
    return render_template('generator.html', form=form)


if __name__ == '__main__':
    app.run()
