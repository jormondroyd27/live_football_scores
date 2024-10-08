from flask import Flask, render_template, url_for
from beautiful_soup import month_and_year, todays_date, match_time, home_teams, away_teams, scores, home_team_score, away_team_score

app = Flask(__name__)

@app.route('/')
def index():
    mmyy = month_and_year()
    date = todays_date()
    kick_off = match_time()
    home_team = home_teams()
    away_team = away_teams()
    score = scores()
    home_team_scores = home_team_score(score)
    away_team_scores = away_team_score(score)
    return render_template('index.html', mmyy=mmyy, date=date, kick_off=kick_off, home_team=home_team, away_team=away_team, home_team_scores=home_team_scores, away_team_scores=away_team_scores, zip=zip)

if __name__ == '__main__':
   app.run()