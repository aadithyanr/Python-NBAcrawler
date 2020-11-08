import requests
from bs4 import BeautifulSoup
#get teamName
def get_teamName(teamInfo):
    return teamInfo.find('span', {'class', 'long-name'}).contents
#get gameScore
def get_gameStatus(game):
    periods = game.find('thead').findAll('th')
    Score = game.find('tbody').findAll('tr')
    away = Score[0].findAll('td')
    home = Score[1].findAll('td')
    index = 0
    for period in periods:
        if(not period.contents):
            periods[index] = 'Team'           
        else:
            periods[index] = period.contents[0]
        
        away[index] = away[index].contents[0]
        home[index] = home[index].contents[0]
        index += 1
    
    return [periods, away, home]

def get_game(gameID):
    res = requests.get('http://www.espn.com/nba/game?gameId=' + gameID)
    soup = BeautifulSoup(res.text, "html.parser")


    teamMatch = soup.find("div", {"id": "gamepackage-matchup-wrap"})#score header
    team_away = get_teamName(teamMatch.find('div', {'class': 'team away'}))
    team_home = get_teamName(teamMatch.find('div', {'class': 'team home'}))
    game_status = get_gameStatus(teamMatch.find('table', {'class', 'miniTable'}))

    return [team_away, team_home, game_status]