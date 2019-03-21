from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, validators
from wtforms.validators import DataRequired

class BiddingForm(FlaskForm):
    server_id = StringField('server_id', validators=[DataRequired()])
    quantity = IntegerField('server qty', [validators.NumberRange(min=0, max=10)])
    wanted_from = StringField('start time', validators=[DataRequired()])
    duration =  IntegerField('hours of use', [validators.NumberRange(min=0, max=10)])
    max_price_quote = IntegerField('max price', [validators.NumberRange(min=0, max=10)])
    submit = SubmitField('Submit Bid')
