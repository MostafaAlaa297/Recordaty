import os

from flask import Flask, flash, redirect, render_template, url_for
from flask_wtf.csrf import CSRFProtect

from forms import ConditionEditForm, LoginForm, ProfileEditForm, RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY',
                                          'my_default_secret_key')

csrf = CSRFProtect(app)


@app.route('/')
@app.route('/home')
def home():
    login_form = LoginForm()
    register_form = RegistrationForm()
    return render_template('home.html',
                           title='Home',
                           login_form=login_form,
                           register_form=register_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # Perform login logic here
        flash('Login requested for user {}, remember_me={}'.format(
            login_form.email.data, login_form.remember.data))
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=login_form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        # Perform registration logic here
        flash('Account created for user {}!'.format(
            registration_form.username.data))
        return redirect(url_for('login'))
    return render_template('register.html',
                           title='Register',
                           form=registration_form)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    profile_form = ProfileEditForm()
    if profile_form.validate_on_submit():
        # Perform profile update logic here
        flash('Profile update!')
        return redirect(url_for('profile'))
    return render_template('profile.html', title='Profile', form=profile_form)


@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    edit_profile_form = ProfileEditForm()
    if edit_profile_form.validate_on_submit():
        # Perform profile update logic here
        flash('Profile updated!')
        return redirect(url_for('profile'))
    else:
        if edit_profile_form.errors:
            flash(str(edit_profile_form.errors), 'error')
    return render_template('edit_profile.html',
                           title='Edit Profile',
                           form=edit_profile_form)


@app.route('/edit_condition', methods=['GET', 'POST'])
def edit_condition():
    edit_condition_form = ConditionEditForm()
    if edit_condition_form.validate_on_submit():
        # Perform profile update logic here
        flash('Condition data updated!')
        return redirect(url_for('profile'))
    else:
        if edit_condition_form.errors:
            flash(str(edit_condition_form.errors), 'error')
    return render_template('edit_condition.html', form=edit_condition_form)


if __name__ == '__main__':
    app.run(debug=True)
