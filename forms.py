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
    rating_ovr = IntegerField("Club's overall rating", validators=[InputRequired()])
    att_form = IntegerField("Club's attack form rating", validators=[InputRequired()])
    def_form = IntegerField("Club's defensive form rating", validators=[InputRequired()])
    set_piece_goals_per_match = IntegerField("How many goals from set pieces per match?", validators=[InputRequired()])
    set_piece_goals_per_match_against = IntegerField("How many goals against from set pieces per match?", validators=[InputRequired()])


class CreateMatchForm(FlaskForm):
    status = StringField("Match status", validators=[InputRequired()])
    completion_status = StringField("Match status", validators=[InputRequired()])
    gameweek = StringField("Match gameweek", validators=[InputRequired()])
    date = StringField("Match date", validators=[InputRequired()])
    time = StringField("Match time", validators=[InputRequired()])
    home_club = StringField("Home club's abbreviated name", validators=[InputRequired()])
    away_club = StringField("Away club's abbreviated name", validators=[InputRequired()])
    home_score = IntegerField("Home club's score", validators=[InputRequired()])
    away_score = IntegerField("Away club's score", validators=[InputRequired()])
    predicted_home_score = IntegerField("Predicted home score", validators=[InputRequired()])
    predicted_away_score = IntegerField("Predicted away score", validators=[InputRequired()])
