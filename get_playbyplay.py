import requests
from bs4 import BeautifulSoup


def CapturePlay(table):
    Play = []
    for index in range(1, len(table)):
        details = table[index].findAll('td')
        temp = []
        for detail in details:
            if detail.contents:
                if isinstance(detail.contents[0], str):
                    temp.append(detail.contents[0])
                else:
                    temp.append(detail.contents[0]['src'])
        Play.append(temp)

    return Play


def Quarter(soup, Q):
    wrapper = soup.find('div', {'id': 'gp-quarter-' + Q})
    table = wrapper.find('table').findAll('tr')
    table = CapturePlay(table)
    return table


def playbyplay(gameID, totalQuarter):
    res = requests.get('http://www.espn.com/nba/playbyplay?gameId=' + gameID)
    soup = BeautifulSoup(res.text, "lxml")

    Play = []

    for Q in range(1, totalQuarter + 1):
        table = Quarter(soup, str(Q))
        Play.append(table)

    return Play
