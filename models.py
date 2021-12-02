from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Clubs(db.Model):
    __tablename__ = "clubs"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    club_name_short = db.Column(db.Text, nullable=True)
    club_name_long = db.Column(db.Text, nullable=True)
    club_logo = db.Column(db.Text, nullable=True)

    wins = db.Column(db.Integer, nullable=True)
    draws = db.Column(db.Integer, nullable=True)
    losses = db.Column(db.Integer, nullable=True)
    played = db.Column(db.Integer, nullable=True)
    points = db.Column(db.Integer, nullable=True)
    goals_for = db.Column(db.Integer, nullable=True)
    goals_against = db.Column(db.Integer, nullable=True)
    position = db.Column(db.Integer, nullable=True)
    set_piece_goals_per_match = db.Column(db.Integer, nullable=True)
    set_piece_goals_per_match_against = db.Column(db.Integer, nullable=True)
    rating_ovr = db.Column(db.Integer, nullable=True)
    att_form = db.Column(db.Integer, nullable=True)
    def_form = db.Column(db.Integer, nullable=True)

class Matches(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    status = db.Column(db.Text, nullable=True)
    completion_status = db.Column(db.Text, nullable=True)
    gameweek = db.Column(db.Text, nullable=True)
    date = db.Column(db.Text, nullable=True)
    time = db.Column(db.Text, nullable=True)
    home_logo = db.Column(db.Text, nullable=True)
    home_club = db.Column(db.Text, nullable=True)
    away_logo = db.Column(db.Text, nullable=True)
    away_club = db.Column(db.Text, nullable=True)
    home_score = db.Column(db.Integer, nullable=True)
    away_score = db.Column(db.Integer, nullable=True)
    home_att_form = db.Column(db.Integer, nullable=True)
    home_def_form = db.Column(db.Integer, nullable=True)
    away_att_form = db.Column(db.Integer, nullable=True)
    away_def_form = db.Column(db.Integer, nullable=True)
    predicted_home_score = db.Column(db.Integer, nullable=True)
    predicted_away_score = db.Column(db.Integer, nullable=True)
