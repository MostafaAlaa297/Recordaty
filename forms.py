from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    DateField,
    MultipleFileField,
    IntegerField,
    PasswordField,
    TimeField,
    SelectField,
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(),
                                        EqualTo('password')])
    age = IntegerField(
        'Age', validators=[DataRequired(),
                           NumberRange(min=1, max=150)])
    gender = SelectField('Gender',
                         choices=[('male', 'Male'), ('female', 'Female')],
                         validators=[DataRequired()])
    phone1 = StringField('Phone number', validators=[DataRequired()])
    phone2 = StringField('Phone number')
    submit = SubmitField('Sign Up')


class ProfileEditForm(FlaskForm):
    name = StringField('Username: ',
                       validators=[DataRequired(),
                                   Length(min=2, max=20)])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    gender = SelectField('Gender',
                         choices=[('male', 'Male'), ('female', 'Female')],
                         validators=[DataRequired()])
    age = IntegerField(
        'Age: ', validators=[DataRequired(),
                             NumberRange(min=1, max=150)])
    phone = StringField('Phone number:', validators=[DataRequired()])
    health_insurance = SelectField(
        'Health Insurance: ',
        choices=[('EPO', ' Exclusive Provider Organization'),
                 ('HMO', 'Health Maintenance Organization'),
                 ('POS', 'Point of Service'),
                 ('PPO', 'Preferred Provider Organization')],
        validators=[DataRequired()])
    weight = IntegerField('Weight: ',
                          validators=[
                              DataRequired(),
                              NumberRange(min=1,
                                          message="Weight must be at least 1.")
                          ])
    height = IntegerField('Height: ',
                          validators=[DataRequired(),
                                      NumberRange(min=1)])
    blood_type = SelectField('Blood Type: ',
                             choices=[('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'),
                                      ('b-', 'B-'), ('ab+', 'AB+'),
                                      ('ab-', 'AB-'), ('o+', 'O+'),
                                      ('o-', 'O-')],
                             validators=[DataRequired()])
    allergies = StringField('Alergies: ', validators=[DataRequired()])
    medications = StringField('Medications: ', validators=[DataRequired()])
    chronic_illnesses = StringField("Chronic Illnesses: ",
                                    validators=[DataRequired()])
    family_medical_history = StringField("Family Medical History: ",
                                         validators=[DataRequired()])
    submit = SubmitField('Edit Profile')


class ConditionEditForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    time = TimeField('Time', validators=[DataRequired(), Email()])
    type = SelectField('Medical Service Type',
                       choices=[('doctor visit', 'Doctor Visit'),
                                ('surgery', 'Surgery'),
                                ('analysis', 'Analysis'),
                                ('raidiology', 'Radiology')],
                       validators=[DataRequired()])
    healthcare_professional_name = StringField('Healthcare Professional Name',
                                               validators=[DataRequired()])
    medical_report = MultipleFileField('Upload File/Files: ',
                                       validators=[DataRequired()])
    submit = SubmitField('Edit Condition')
