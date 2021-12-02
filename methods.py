import requests
from models import connect_db, db, Clubs, Matches
# Filling our Clubs database in one go
# make an epl dict
# loop through the dict
# commit club info to database


#guidance
	#Every team has a goal to give to it's opponent, 1 goal for or against does not effect form
	#after 1 goal, the next goal is worth 0.5 points +/- goals for/goals against
	#if a club fails to score it is -0.5 last_match.goals_for
	#if a club gets a clean sheet it is +0.5 last_match.goals_for


# API CALL
def import_fantasy_data():
    res = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
    data = res.json()
    return data


fantasy = import_fantasy_data()

# CATEGORIZE THE DATA
teams = fantasy['teams']
players = fantasy['elements']


# BUILD CLUBS ***********************************************************************
clubs = [
    {
        "club_name_short": "MCY",
        "club_name_long": "Manchester City",
        "club_logo": "/static/img/ManchesterCity_wbg.png.cf.jpg",
        "wins": 10,
        "draws": 2,
        "losses": 2,
        "played": 14,
        "points": 32,
        "goals_for": 29,
        "goals_against": 8,
        "position": 2,
        "rating_ovr": 85,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "LIV",
        "club_name_long": "Liverpool",
        "club_logo": "/static/img/Liverpool_wbg.png.cf.jpg",
        "wins": 9,
        "draws": 4,
        "losses": 1,
        "played": 14,
        "points": 31,
        "goals_for": 43,
        "goals_against": 12,
        "position": 3,
        "rating_ovr": 84,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "MNU",
        "club_name_long": "Manchester United",
        "club_logo": "/static/img/ManchesterUnited_wbg.png.cf.jpg",
        "wins": 5,
        "draws": 3,
        "losses": 5,
        "played": 13,
        "points": 18,
        "goals_for": 21,
        "goals_against": 22,
        "position": 8,
        "rating_ovr": 84,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "CHE",
        "club_name_long": "Chelsea",
        "club_logo": "/static/img/Chelsea_wbg.png.cf.jpg",
        "wins": 10,
        "draws": 3,
        "losses": 1,
        "played": 14,
        "points": 33,
        "goals_for": 33,
        "goals_against": 6,
        "position": 1,
        "rating_ovr": 83,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "TOT",
        "club_name_long": "Tottenham",
        "club_logo": "/static/img/Tottenham_wbg.png.cf.jpg",
        "wins": 6,
        "draws": 1,
        "losses": 5,
        "played": 12,
        "points": 19,
        "goals_for": 11,
        "goals_against": 17,
        "position": 7,
        "rating_ovr": 81,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "LEI",
        "club_name_long": "Leicester City",
        "club_logo": "/static/img/LeicesterCity_wbg.png.cf.jpg",
        "wins": 5,
        "draws": 4,
        "losses": 5,
        "played": 14,
        "points": 19,
        "goals_for": 22,
        "goals_against": 25,
        "position": 10,
        "rating_ovr": 80,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "ARS",
        "club_name_long": "Arsenal",
        "club_logo": "/static/img/Arsenal_wbg.png.cf.jpg",
        "wins": 7,
        "draws": 2,
        "losses": 4,
        "played": 13,
        "points": 23,
        "goals_for": 15,
        "goals_against": 17,
        "position": 5,
        "rating_ovr": 79,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "WHU",
        "club_name_long": "West Ham United",
        "club_logo": "/static/img/WestHam_wbg.png.cf.jpg",
        "wins": 7,
        "draws": 3,
        "losses": 4,
        "played": 14,
        "points": 24,
        "goals_for": 25,
        "goals_against": 17,
        "position": 4,
        "rating_ovr": 79,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "EVE",
        "club_name_long": "Everton",
        "club_logo": "/static/img/Everton_wbg.png.cf.jpg",
        "wins": 4,
        "draws": 3,
        "losses": 7,
        "played": 14,
        "points": 15,
        "goals_for": 17,
        "goals_against": 24,
        "position": 14,
        "rating_ovr": 79,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "AVA",
        "club_name_long": "Aston Villa",
        "club_logo": "/static/img/AstonVilla2_wbg.png.cf.jpg",
        "wins": 5,
        "draws": 1,
        "losses": 8,
        "played": 14,
        "points": 16,
        "goals_for": 19,
        "goals_against": 23,
        "position": 13,
        "rating_ovr": 76,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "WOL",
        "club_name_long": "Wolverhampton Wanderers",
        "club_logo": "/static/img/Wolverhampton2_wbg.png.cf.jpg",
        "wins": 6,
        "draws": 3,
        "losses": 5,
        "played": 14,
        "points": 21,
        "goals_for": 12,
        "goals_against": 12,
        "position": 6,
        "rating_ovr": 78,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "NEW",
        "club_name_long": "Newcastle United",
        "club_logo": "/static/img/Newcastle2_wbg.png.cf.jpg",
        "wins": 0,
        "draws": 7,
        "losses": 7,
        "played": 14,
        "points": 7,
        "goals_for": 16,
        "goals_against": 30,
        "position": 20,
        "rating_ovr": 76,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "LEE",
        "club_name_long": "Leeds United",
        "club_logo": "/static/img/LeedsUnited_wbg.png.cf.jpg",
        "wins": 3,
        "draws": 6,
        "losses": 5,
        "played": 14,
        "points": 15,
        "goals_for": 13,
        "goals_against": 20,
        "position": 17,
        "rating_ovr": 76,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "CRY",
        "club_name_long": "Crystal Palace",
        "club_logo": "/static/img/CrystalPalace_wbg.png.cf.jpg",
        "wins": 3,
        "draws": 7,
        "losses": 4,
        "played": 14,
        "points": 16,
        "goals_for": 19,
        "goals_against": 20,
        "position": 11,
        "rating_ovr": 76,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "BRI",
        "club_name_long": "Brighton Hove Albion",
        "club_logo": "/static/img/BrightonHoveAlbion_wbg.png.cf.jpg",
        "wins": 4,
        "draws": 7,
        "losses": 3,
        "played": 14,
        "points": 19,
        "goals_for": 13,
        "goals_against": 15,
        "position": 9,
        "rating_ovr": 76,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "SOU",
        "club_name_long": "Southampton",
        "club_logo": "/static/img/Southampton_wbg.png.cf.jpg",
        "wins": 3,
        "draws": 6,
        "losses": 5,
        "played": 14,
        "points": 15,
        "goals_for": 13,
        "goals_against": 20,
        "position": 15,
        "rating_ovr": 76,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "BUR",
        "club_name_long": "Burnley",
        "club_logo": "/static/img/Burnley_wbg.png.cf.jpg",
        "wins": 1,
        "draws": 7,
        "losses": 5,
        "played": 14,
        "points": 10,
        "goals_for": 14,
        "goals_against": 20,
        "position": 18,
        "rating_ovr": 76,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "WAT",
        "club_name_long": "Watford",
        "club_logo": "/static/img/Watford_wbg.png.cf.jpg",
        "wins": 4,
        "draws": 1,
        "losses": 9,
        "played": 14,
        "points": 13,
        "goals_for": 19,
        "goals_against": 26,
        "position": 16,
        "rating_ovr": 75,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "NOR",
        "club_name_long": "Norwich City",
        "club_logo": "/static/img/NorwichCity_wbg.png.cf.jpg",
        "wins": 2,
        "draws": 4,
        "losses": 8,
        "played": 14,
        "points": 10,
        "goals_for": 8,
        "goals_against": 27,
        "position": 19,
        "rating_ovr": 74,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
    {
        "club_name_short": "BRE",
        "club_name_long": "Brentford",
        "club_logo": "/static/img/Brentford_wbg.png.cf.jpg",
        "wins": 4,
        "draws": 4,
        "losses": 5,
        "played": 13,
        "points": 16,
        "goals_for": 17,
        "goals_against": 17,
        "position": 12,
        "rating_ovr": 73,
        "att_form": 5,
        "def_form": 5,
        "set_piece_goals_per_match": 0,
        "set_piece_goals_per_match_against": 0,
    },
]

# build a team's strength based on player's form
for player in players:
    for club in clubs:

        # ARSENAL TEAM
        if player['team'] == 1 and player['element_type'] > 2:
            if club['club_name_short'] == 'ARS':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 1 and player['element_type'] < 3:
            if club['club_name_short'] == 'ARS':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # ASTON VILLA TEAM
        if player['team'] == 2 and player['element_type'] > 2:
            if club['club_name_short'] == 'AVA':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 2 and player['element_type'] < 3:
            if club['club_name_short'] == 'AVA':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # BRENTFORD TEAM
        if player['team'] == 3 and player['element_type'] > 2:
            if club['club_name_short'] == 'BRE':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 3 and player['element_type'] < 3:
            if club['club_name_short'] == 'BRE':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # BRIGHTON TEAM
        if player['team'] == 4 and player['element_type'] > 2:
            if club['club_name_short'] == 'BRI':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 4 and player['element_type'] < 3:
            if club['club_name_short'] == 'BRI':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # BURNLEY TEAM
        if player['team'] == 5 and player['element_type'] > 2:
            if club['club_name_short'] == 'BUR':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 5 and player['element_type'] < 3:
            if club['club_name_short'] == 'BUR':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # CHELSEA TEAM
        if player['team'] == 6 and player['element_type'] > 2:
            if club['club_name_short'] == 'CHE':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 6 and player['element_type'] < 3:
            if club['club_name_short'] == 'CHE':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # CRYSTAL PALACE TEAM
        if player['team'] == 7 and player['element_type'] > 2:
            if club['club_name_short'] == 'CRY':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 7 and player['element_type'] < 3:
            if club['club_name_short'] == 'CRY':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # EVERTON TEAM
        if player['team'] == 8 and player['element_type'] > 2:
            if club['club_name_short'] == 'EVE':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 8 and player['element_type'] < 3:
            if club['club_name_short'] == 'EVE':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # LEICESTER TEAM
        if player['team'] == 9 and player['element_type'] > 2:
            if club['club_name_short'] == 'LEI':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 9 and player['element_type'] < 3:
            if club['club_name_short'] == 'LEI':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # LEEDS TEAM
        if player['team'] == 10 and player['element_type'] > 2:
            if club['club_name_short'] == 'LEE':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 10 and player['element_type'] < 3:
            if club['club_name_short'] == 'LEE':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # LIVERPOOL TEAM
        if player['team'] == 11 and player['element_type'] > 2:
            if club['club_name_short'] == 'LIV':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 11 and player['element_type'] < 3:
            if club['club_name_short'] == 'LIV':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # MAN CITY TEAM
        if player['team'] == 12 and player['element_type'] > 2:
            if club['club_name_short'] == 'MCY':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 12 and player['element_type'] < 3:
            if club['club_name_short'] == 'MCY':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # MAN UNITED TEAM
        if player['team'] == 13 and player['element_type'] > 2:
            if club['club_name_short'] == 'MNU':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 13 and player['element_type'] < 3:
            if club['club_name_short'] == 'MNU':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # NEWCASTLE TEAM
        if player['team'] == 14 and player['element_type'] > 2:
            if club['club_name_short'] == 'NEW':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 14 and player['element_type'] < 3:
            if club['club_name_short'] == 'NEW':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # NORWICH TEAM
        if player['team'] == 15 and player['element_type'] > 2:
            if club['club_name_short'] == 'NOR':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 15 and player['element_type'] < 3:
            if club['club_name_short'] == 'NOR':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['att_form'], 2)

        # SOUTHAMPTON TEAM
        if player['team'] == 16 and player['element_type'] > 2:
            if club['club_name_short'] == 'SOU':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 16 and player['element_type'] < 3:
            if club['club_name_short'] == 'SOU':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # SPURS TEAM
        if player['team'] == 17 and player['element_type'] > 2:
            if club['club_name_short'] == 'TOT':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 17 and player['element_type'] < 3:
            if club['club_name_short'] == 'TOT':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # WATFORD TEAM
        if player['team'] == 18 and player['element_type'] > 2:
            if club['club_name_short'] == 'WAT':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 18 and player['element_type'] < 3:
            if club['club_name_short'] == 'WAT':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # WEST HAM TEAM
        if player['team'] == 19 and player['element_type'] > 2:
            if club['club_name_short'] == 'WHU':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 19 and player['element_type'] < 3:
            if club['club_name_short'] == 'WHU':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

        # WOLVES TEAM
        if player['team'] == 20 and player['element_type'] > 2:
            if club['club_name_short'] == 'WOL':
                club['att_form'] += float(player['form'])
                club['att_form'] = round(club['att_form'], 2)
        if player['team'] == 20 and player['element_type'] < 3:
            if club['club_name_short'] == 'WOL':
                club['def_form'] += float(player['form'])
                club['def_form'] = round(club['def_form'], 2)

# add club info to datbase
def add_clubs():
    db.drop_all()
    db.create_all()
    for club in clubs:
        new_club = Clubs(
            club_name_short=club['club_name_short'],
            club_name_long=club['club_name_long'],
            club_logo=club['club_logo'],
            wins=club['wins'],
            losses=club['losses'],
            draws=club['draws'],
            played=club['played'],
            points=club['points'],
            position=club['position'],
            goals_for=club['goals_for'],
            goals_against=club['goals_against'],
            rating_ovr=club['rating_ovr'],
            att_form=club['att_form'],
            def_form=club['def_form'],
            set_piece_goals_per_match=club['set_piece_goals_per_match'],
            set_piece_goals_per_match_against=club['set_piece_goals_per_match_against']
        )

        # add and commit the new club to our datbase
        db.session.add(new_club)
        db.session.commit()


# BUILD MATCHES *********************************************************************
# epl matches for the season
epl_matches = [
    {
        'status': 'complete',
        'gameweek': "Game Week 11",
        'matchlist': [
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 11',
                "date": '11/05/2021',
                "time": '6:30 AM',
                "home_club": 'SOU',
                "away_club": 'AVA',
                "home_logo": '',
                "away_logo": '',
                "home_score": 1,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 11',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'MNU',
                "away_club": 'MCY',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 2,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 11',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'BRE',
                "away_club": 'NOR',
                "home_logo": '',
                "away_logo": '',
                "home_score": 1,
                "away_score": 2,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 11',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'CHE',
                "away_club": 'BUR',
                "home_logo": '',
                "away_logo": '',
                "home_score": 1,
                "away_score": 1,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 11',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'CRY',
                "away_club": 'WOL',
                "home_logo": '',
                "away_logo": '',
                "home_score": 2,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 11',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'WOL',
                "away_club": 'LIV',
                "home_logo": '',
                "away_logo": '',
                "home_score": 3,
                "away_score": 2,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 11',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'BRI',
                "away_club": 'NEW',
                "home_logo": '',
                "away_logo": '',
                "home_score": 1,
                "away_score": 1,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 11',
                "date": '11/20/2021',
                "time": '11:30 AM',
                "home_club": 'EVE',
                "away_club": 'TOT',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 11',
                "date": '11/21/2021',
                "time": '8:00 AM',
                "home_club": 'LEE',
                "away_club": 'LEI',
                "home_logo": '',
                "away_logo": '',
                "home_score": 1,
                "away_score": 1,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 11',
                "date": '11/21/2021',
                "time": '10:30 AM',
                "home_club": 'ARS',
                "away_club": 'WAT',
                "home_logo": '',
                "away_logo": '',
                "home_score": 1,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
        ]
    },
    {
        'status': 'complete',
        'gameweek': "Game Week 12",
        'matchlist': [
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 12',
                "date": '11/20/2021',
                "time": '6:30 AM',
                "home_club": 'LEI',
                "away_club": 'CHE',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 3,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 12',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'NEW',
                "away_club": 'BRE',
                "home_logo": '',
                "away_logo": '',
                "home_score": 3,
                "away_score": 3,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 12',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'BUR',
                "away_club": 'CRY',
                "home_logo": '',
                "away_logo": '',
                "home_score": 3,
                "away_score": 3,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 12',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'AVA',
                "away_club": 'BRI',
                "home_logo": '',
                "away_logo": '',
                "home_score": 2,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 12',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'WAT',
                "away_club": 'MNU',
                "home_logo": '',
                "away_logo": '',
                "home_score": 4,
                "away_score": 1,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 12',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'WOL',
                "away_club": 'WHU',
                "home_logo": '',
                "away_logo": '',
                "home_score": 1,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 12',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'NOR',
                "away_club": 'SOU',
                "home_logo": '',
                "away_logo": '',
                "home_score": 2,
                "away_score": 1,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek":'Gameweek 12',
                "date": '11/20/2021',
                "time": '11:30 AM',
                "home_club": 'LIV',
                "away_club": 'ARS',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek": 'Gameweek 12',
                "date": '11/21/2021',
                "time": '8:00 AM',
                "home_club": 'MCY',
                "away_club": 'EVE',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek": 'Gameweek 12',
                "date": '11/21/2021',
                "time": '10:30 AM',
                "home_club": 'TOT',
                "away_club": 'LEE',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
        ]
    },
    {
        'status': 'last',
        'gameweek': "Game Week 13",
        'matchlist': [
            {
                "status": "final",
                "completion_status": "final",
                "gameweek": 'Gameweek 13',
                "date": '11/20/2021',
                "time": '6:30 AM',
                "home_club": 'LEI',
                "away_club": 'CHE',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek": 'Gameweek 13',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'NEW',
                "away_club": 'BRE',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek": 'Gameweek 13',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'BUR',
                "away_club": 'CRY',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek": 'Gameweek 13',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'AVA',
                "away_club": 'BRI',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek": 'Gameweek 13',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'WAT',
                "away_club": 'MNU',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek": 'Gameweek 13',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'WOL',
                "away_club": 'WHU',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek": 'Gameweek 13',
                "date": '11/20/2021',
                "time": '9:00 AM',
                "home_club": 'NOR',
                "away_club": 'SOU',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek": 'Gameweek 13',
                "date": '11/20/2021',
                "time": '11:30 AM',
                "home_club": 'LIV',
                "away_club": 'ARS',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek": 'Gameweek 13',
                "date": '11/21/2021',
                "time": '8:00 AM',
                "home_club": 'MCY',
                "away_club": 'EVE',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "final",
                "completion_status": "final",
                "gameweek": 'Gameweek 13',
                "date": '11/21/2021',
                "time": '10:30 AM',
                "home_club": 'TOT',
                "away_club": 'LEE',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
        ]
    },
    {
        'status': 'next',
        'gameweek': "Game Week 14",
        'matchlist': [
            {
                "status": "next",
                "completion_status": "final",
                "gameweek": 'Gameweek 14',
                "date": '11/30/2021',
                "time": '1:30 PM',
                "home_club": 'NEW',
                "away_club": 'NOR',
                "home_logo": '',
                "away_logo": '',
                "home_score": 1,
                "away_score": 1,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,

            },
            {
                "status": "next",
                "completion_status": "final",
                "gameweek": 'Gameweek 14',
                "date": '11/30/2021',
                "time": '2:15 PM',
                "home_club": 'LEE',
                "away_club": 'CRY',
                "home_logo": '',
                "away_logo": '',
                "home_score": 1,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "next",
                "completion_status": "final",
                "gameweek": 'Gameweek 14',
                "date": '12/01/2021',
                "time": '1:30 PM',
                "home_club": 'WAT',
                "away_club": 'CHE',
                "home_logo": '',
                "away_logo": '',
                "home_score": 1,
                "away_score": 2,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "next",
                "completion_status": "final",
                "gameweek": 'Gameweek 14',
                "date": '12/01/2021',
                "time": '1:30 PM',
                "home_club": 'WHU',
                "away_club": 'BRI',
                "home_logo": '',
                "away_logo": '',
                "home_score": 1,
                "away_score": 1,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "next",
                "completion_status": "final",
                "gameweek": 'Gameweek 14',
                "date": '12/01/2021',
                "time": '1:30 PM',
                "home_club": 'WOL',
                "away_club": 'BUR',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "next",
                "completion_status": "final",
                "gameweek": 'Gameweek 14',
                "date": '12/01/2021',
                "time": '1:30 PM',
                "home_club": 'SOU',
                "away_club": 'LEI',
                "home_logo": '',
                "away_logo": '',
                "home_score": 2,
                "away_score": 2,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "next",
                "completion_status": "final",
                "gameweek": 'Gameweek 14',
                "date": '12/01/2021',
                "time": '2:15 PM',
                "home_club": 'AVA',
                "away_club": 'MCY',
                "home_logo": '',
                "away_logo": '',
                "home_score": 1,
                "away_score": 2,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "next",
                "completion_status": "final",
                "gameweek": 'Gameweek 14',
                "date": '12/01/2021',
                "time": '2:15 PM',
                "home_club": 'EVE',
                "away_club": 'LIV',
                "home_logo": '',
                "away_logo": '',
                "home_score": 1,
                "away_score": 4,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "next",
                "completion_status": "pending",
                "gameweek": 'Gameweek 14',
                "date": '12/02/2021',
                "time": '1:30 PM',
                "home_club": 'TOT',
                "away_club": 'BRE',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "next",
                "completion_status": "pending",
                "gameweek": 'Gameweek 14',
                "date": '12/01/2021',
                "time": '2:15 PM',
                "home_club": 'MNU',
                "away_club": 'ARS',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            }
        ]
    },
    {
        'status': 'upcoming',
        'gameweek': "Game Week 15",
        'matchlist': [
            {
                "status": "pending",
                "completion_status": "pending",
                "gameweek": 'Gameweek 15',
                "date": '12/04/2021',
                "time": '6:30 AM',
                "home_club": 'WHU',
                "away_club": 'CHE',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "pending",
                "completion_status": "pending",
                "gameweek": 'Gameweek 15',
                "date": '12/04/2021',
                "time": '9:00 AM',
                "home_club": 'NEW',
                "away_club": 'BUR',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "pending",
                "completion_status": "pending",
                "gameweek": 'Gameweek 15',
                "date": '12/04/2021',
                "time": '9:00 AM',
                "home_club": 'SOU',
                "away_club": 'BRI',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "pending",
                "completion_status": "pending",
                "gameweek": 'Gameweek 15',
                "date": '12/04/2021',
                "time": '9:00 AM',
                "home_club": 'WOL',
                "away_club": 'LIV',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "pending",
                "completion_status": "pending",
                "gameweek": 'Gameweek 15',
                "date": '12/04/2021',
                "time": '11:30 AM',
                "home_club": 'WAT',
                "away_club": 'MCY',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "pending",
                "completion_status": "pending",
                "gameweek": 'Gameweek 15',
                "date": '12/05/2021',
                "time": '8:00 AM',
                "home_club": 'TOT',
                "away_club": 'NOR',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "pending",
                "completion_status": "pending",
                "gameweek": 'Gameweek 15',
                "date": '12/05/2021',
                "time": '8:00 AM',
                "home_club": 'LEE',
                "away_club": 'BRE',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "pending",
                "completion_status": "pending",
                "gameweek": 'Gameweek 15',
                "date": '12/05/2021',
                "time": '8:00 AM',
                "home_club": 'MNU',
                "away_club": 'CRY',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "pending",
                "completion_status": "pending",
                "gameweek": 'Gameweek 15',
                "date": '12/05/2021',
                "time": '8:00 AM',
                "home_club": 'AVA',
                "away_club": 'LEI',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            },
            {
                "status": "pending",
                "completion_status": "pending",
                "gameweek": 'Gameweek 15',
                "date": '12/06/2021',
                "time": '2:00 PM',
                "home_club": 'EVE',
                "away_club": 'ARS',
                "home_logo": '',
                "away_logo": '',
                "home_score": 0,
                "away_score": 0,
                "home_att_form": 0,
                "home_def_form": 0,
                "away_att_form": 0,
                "away_def_form": 0,
                "predicted_home_score": 0,
                "predicted_away_score": 0,
            }
        ]
    }
]

# make predictions for goals
for week in epl_matches:
    if week['status'] == 'next':
        for match in week['matchlist']:
            for club in clubs:
                if match['home_club'] == club['club_name_short']:
                    match['home_att_form'] = club['att_form']
                    match['home_def_form'] = club['def_form']
                    match['home_logo'] = club['club_logo']

                if match['away_club'] == club['club_name_short']:
                    match['away_att_form'] = club['att_form']
                    match['away_def_form'] = club['def_form']
                    match['away_logo'] = club['club_logo']

                # home goal predictions
                if match['home_att_form'] - match['away_def_form'] >= 2:
                    match['predicted_home_score'] = 1
                    match['away_def_form'] += 5
                if match['home_att_form'] - match['away_def_form'] >= 3:
                    match['predicted_home_score'] = 2
                    match['away_def_form'] += 3
                if match['home_att_form'] - match['away_def_form'] >= 4:
                    match['predicted_home_score'] = 3
                    match['away_def_form'] += 3
                if match['home_att_form'] - match['away_def_form'] >= 5:
                    match['predicted_home_score'] = 4


                # away goal prediction
                if match['away_att_form'] - match['home_def_form'] >= 2:
                    match['predicted_away_score'] = 1
                    match['home_def_form'] += 5
                if match['away_att_form'] - match['home_def_form'] >= 3:
                    match['predicted_away_score'] = 2
                    match['home_def_form'] += 3
                if match['away_att_form'] - match['home_def_form'] >= 4:
                    match['predicted_away_score'] = 3
                    match['home_def_form'] += 3
                if match['away_att_form'] - match['home_def_form'] >= 5:
                    match['predicted_away_score'] = 3

# add matches to database
def add_matches():
    Matches.__table__.drop(db.engine)
    Matches.__table__.create(db.engine)
    for week in epl_matches:
        for match in week['matchlist']:
            new_match = Matches(
                status=match['status'],
                completion_status=match['completion_status'],
                gameweek=match['gameweek'],
                date=match['date'],
                time=match['time'],
                home_club=match['home_club'],
                away_club=match['away_club'],
                home_logo=match['home_logo'],
                away_logo=match['away_logo'],
                home_score=match['home_score'],
                away_score=match['away_score'],
                home_att_form=match["home_att_form"],
                home_def_form=match["home_def_form"],
                away_att_form=match["away_att_form"],
                away_def_form=match["away_def_form"],
                predicted_home_score=match['predicted_home_score'],
                predicted_away_score=match['predicted_away_score']
            )

            # add and commit the new club to our datbase
            db.session.add(new_match)
            db.session.commit()


# PRE-LIMINARY TESTING ***********************************************************************
