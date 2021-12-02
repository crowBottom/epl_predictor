from flask import Flask, flash, render_template, redirect, session
from models import connect_db, db, Clubs, Matches
from forms import CreateClubForm, CreateMatchForm
from methods import *
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///epl_predictor_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'crowBottom'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

# Root ROUTE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@app.route('/')
def root_route():
    # update club stats based on previous weeks results
    # update_stats()
    # make predictions for the current week
    add_matches()
    return redirect('/predictions')


# Main ROUTES ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# predictions route
@app.route('/predictions')
def predictions_route():
    matches = Matches.query.all()
    clubs = Clubs.query.all()
    return render_template('predictions.html', matches=matches, clubs=clubs, epl_matches=epl_matches)

# previous weeks route
@app.route('/previous_weeks')
def previous_weeks_route():
    matches = Matches.query.all()
    return render_template('previous_weeks.html', matches=matches)

# standings route
@app.route('/standings')
def standings_route():
    clubs =  Clubs.query.order_by(Clubs.position).all()
    return render_template('standings.html', clubs=clubs)

# seed clubs route
@app.route('/seed/clubs')
def seed_clubs_route():
    add_clubs()
    return redirect('/all_clubs')

# seed matches route
@app.route('/seed/matches')
def seed_matches_route():
    add_matches()
    return redirect('/all_matches')



# RESTFUL ROUTES ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# CLUBS
# GET all clubs
@app.route('/all_clubs')
def get_clubs():
    clubs = Clubs.query.all()
    return render_template('clubs/all_clubs.html', clubs=clubs)

# GET a club
# POST a club
@app.route('/new_club', methods=['GET', 'POST'])
def create_club_route():
    clubs = Clubs.query.all()

    # using flask-what-the-forms here
    form = CreateClubForm()

    # grabbing the form data for use in our create_profile method
    if form.validate_on_submit():
        club_name_short = form.club_name_short.data
        club_name_long = form.club_name_long.data
        club_logo = form.club_logo.data
        wins = form.wins.data
        losses = form.losses.data
        draws = form.draws.data
        played = form.played.data
        points = form.points.data
        goals_for = form.goals_for.data
        goals_against = form.goals_against.data
        position = form.position.data
        rating_ovr = form.rating_ovr.data
        att_form = form.home_form.data
        def_form = form.away_form.data
        set_piece_goals_per_match = form.set_piece_goals_per_match.data
        set_piece_goals_per_match_against = form.set_piece_goals_per_match_against.data

        new_club = Clubs(
            club_name_short=club_name_short,
            club_name_long=club_name_long,
            club_logo=club_logo,
            wins=wins,
            draws=draws,
            losses=losses,
            played=played,
            points=points,
            goals_for=goals_for,
            goals_against=goals_against,
            rating_ovr=rating_ovr,
            att_form=att_form,
            def_form=def_form,
            set_piece_goals_per_match=set_piece_goals_per_match,
            set_piece_goals_per_match_against=set_piece_goals_per_match_against
        )

        # add and commit the new club to our datbase
        db.session.add(new_club)
        db.session.commit()

        return redirect('/new_club')

    # if the form hasn't been submitted yet render the register html
    return render_template('clubs/create_club.html', form=form, clubs=clubs)

# PATCH a club
@app.route('/patch/<int:id>', methods=['GET', 'POST'])
def patch_club(id):
    clubs = Clubs.query.all()
    club = Clubs.query.get_or_404(id)
    # using flask-what-the-forms here
    form = CreateClubForm(obj=club)

    # grabbing the form data for use in our create_profile method
    if form.validate_on_submit():
        club.club_name_short = form.club_name_short.data
        club.club_name_long = form.club_name_long.data
        club.club_logo = form.club_logo.data
        club.wins = form.wins.data
        club.draws = form.draws.data
        club.losses = form.losses.data
        club.played = form.played.data
        club.points = form.points.data
        club.goals_for = form.goals_for.data
        club.goals_against = form.goals_against.data
        club.position = form.position.data
        club.rating_ovr = form.rating_ovr.data
        club.att_form = form.att_form.data
        club.def_form = form.def_form.data

        # commit the edited club to our datbase
        db.session.commit()

        return redirect('/all_clubs')

    # if the form hasn't been submitted yet render the register html
    return render_template('clubs/patch_club.html', form=form,club=club, clubs=clubs)

# DELETE a club
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_club(id):
    club = Clubs.query.get_or_404(id)
    db.session.delete(club)
    db.session.commit()
    return redirect('/all_clubs')

################################################################################

# MATCHES
# GET all matches
@app.route('/all_matches')
def get_matches():
    matches = Matches.query.all()
    return render_template('matches/all_matches.html', matches=matches)

# UPDATE a match
@app.route('/update/<int:id>/match', methods=['GET', 'POST'])
def update_match(id):
    matches = Matches.query.all()
    match = Matches.query.get_or_404(id)
    # using flask-what-the-forms here
    form = CreateMatchForm(obj=match)

    # grabbing the form data for use in our create_profile method
    if form.validate_on_submit():
        match.status = form.status.data
        match.completion_status = form.completion_status.data
        match.gameweek = form.gameweek.data
        match.date = form.date.data
        match.time = form.time.data
        match.home_club = form.home_club.data
        match.away_club = form.away_club.data
        match.home_logo = form.home_logo.data
        match.away_logo = form.away_logo.data
        match.home_score = form.home_score.data
        match.away_score = form.away_score.data
        match.home_att_form = form.home_att_form.data
        match.home_def_form = form.home_def_form.data
        match.away_att_form = form.away_att_form.data
        match.away_def_form = form.away_def_form.data
        match.predicted_home_score = form.predicted_home_score.data
        match.predicted_away_score = form.predicted_away_score.data

        # commit the edited matches to our datbase
        db.session.commit()

        return redirect('/all_matches')

    # if the form hasn't been submitted yet render the register html
    return render_template('matches/update.html', form=form, match=match, matches=matches)

# DELETE a match
@app.route('/delete/<int:id>/match', methods=['GET', 'POST'])
def delete_match(id):
    match  = Matches.query.get_or_404(id)
    db.session.delete(match)
    db.session.commit()
    return redirect('/all_matches')
