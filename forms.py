from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, TextAreaField
from wtforms.validators import InputRequired

class CreateClubForm(FlaskForm):
    club_name_short = StringField("Club's abbreviated name", validators=[InputRequired()])
    club_name_long = StringField("Club's proper name", validators=[InputRequired()])
    club_logo = StringField("Club's logo", validators=[InputRequired()])
    wins = IntegerField("Number of wins", validators=[InputRequired()])
    draws = IntegerField("Number of draws", validators=[InputRequired()])
    losses = IntegerField("Number of losses", validators=[InputRequired()])
    played = IntegerField("Matches played", validators=[InputRequired()])
    points = IntegerField("Number of points", validators=[InputRequired()])
    goals_for = IntegerField("Number of goals for", validators=[InputRequired()])
    goals_against = IntegerField("Number of goals against", validators=[InputRequired()])
    position = IntegerField("Position in the table", validators=[InputRequired()])
    attack = IntegerField("Club's attack rating", validators=[InputRequired()])
    midfield = IntegerField("Club's midfield rating", validators=[InputRequired()])
    defense= IntegerField("Club's defensive rating", validators=[InputRequired()])
    rating_ovr = IntegerField("Club's overall rating", validators=[InputRequired()])
    home_form = IntegerField("Club's home form rating", validators=[InputRequired()])
    away_form = IntegerField("Club's away form rating", validators=[InputRequired()])
