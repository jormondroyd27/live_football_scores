import httpx
from bs4 import BeautifulSoup

a = httpx.get('https://www.skysports.com/football-fixtures')
soup = BeautifulSoup(a.text, features="html.parser")

def month_and_year():
    mmyy = soup.find(class_="fixres__header1")
    return mmyy.text

def todays_date():
    date = soup.find(class_="fixres__header2")
    return date.text

def home_teams():
    home_team_list = []
    for x in soup.find_all('span', class_="matches__participant--side1"):  
        home_team_list.append(x.text)
    home_team_list = [i.strip('\n ') for i in home_team_list]
    return home_team_list

def away_teams():
    away_team_list = []
    for x in soup.find_all('span', class_="matches__participant--side2"):  
        away_team_list.append(x.text)
    away_team_list = [i.strip('\n ') for i in away_team_list]
    return away_team_list

def scores():
    scores = []
    for i in soup.find_all('span', class_="matches__teamscores-side"):
        scores.append(i.text) 
    scores = [i.strip('\n ') for i in scores]
    return scores

def home_team_score(scores):
    home_team_score = []
    for x in range(0, len(scores), 2): 
        home_team_score.append(scores[x])
    return home_team_score

def away_team_score(scores):
    away_team_score = []
    for x in range(1, len(scores), 2): 
        away_team_score.append(scores[x])
    return away_team_score