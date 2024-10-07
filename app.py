from flask import Flask, render_template, url_for
from beautiful_soup import month_and_year, todays_date, home_teams, away_teams, scores, home_team_score, away_team_score

app = Flask(__name__)

@app.route('/')
def index():
    mmyy = month_and_year()
    date = todays_date()
    home_team = home_teams()
    away_team = away_teams()
    score = scores()
    home_team_scores = home_team_score(score)
    away_team_scores = away_team_score(score)
    return render_template('index.html', mmyy=mmyy, date=date, home_team=home_team, away_team=away_team, home_team_scores=home_team_scores, away_team_scores=away_team_scores, zip=zip)

if __name__ == '__main__':
   app.run()