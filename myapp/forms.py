from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class TopCities(FlaskForm):
    city_name = StringField('City Name', validators=[DataRequired()])
    city_rank = IntegerField('City Rank', validators=[DataRequired()])
    is_visited = BooleanField('Is Visited')
    comments = StringField('Comments')

    submit = SubmitField("Submit")
