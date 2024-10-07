import httpx
from bs4 import BeautifulSoup

# this is a terminal application only and is not used for Flask
def main():
    a = httpx.get('https://www.skysports.com/football-fixtures')
    soup = BeautifulSoup(a.text, features="html.parser")

    home_team_list = []
    for x in soup.find_all('span', class_="matches__participant--side1"):  
        home_team_list.append(x.text)
    away_team_list = []
    for x in soup.find_all('span', class_="matches__participant--side2"):  
        away_team_list.append(x.text)
    home_team_list = [i.strip('\n ') for i in home_team_list]
    away_team_list = [i.strip('\n ') for i in away_team_list]

    scores = []
    for i in soup.find_all('span', class_="matches__teamscores-side"):
        scores.append(i.text) 
    scores = [i.strip('\n ') for i in scores]
    
    home_team_score = []
    for x in range(0, len(scores), 2): 
        home_team_score.append(scores[x])

    away_team_score = []
    for x in range(1, len(scores), 2): 
        away_team_score.append(scores[x])

    for home_team, away_team, home_score, away_score in zip(home_team_list, away_team_list, home_team_score, away_team_score):
        print(f'{home_team} {home_score} - {away_score} {away_team}') 
    
if __name__ == '__main__':
    main()