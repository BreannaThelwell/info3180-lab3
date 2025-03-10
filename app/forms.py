#file for form creation

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),Length(min=2, max=50)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(),Length(max=100)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Send')
