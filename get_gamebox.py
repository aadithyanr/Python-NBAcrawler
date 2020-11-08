import requests
from bs4 import BeautifulSoup


def get_wrapper(soup, team):
    wrapper = soup.find('div', {'class', team})
    scoretable = wrapper.find('table')

    def score_thead(head):
        index = 0
        for inner in head:
            head[index] = inner.contents[0]
            index += 1
        return head

    def score_tbody(body, cheak):

        index = 0

        length = len(body)
        if(cheak == 'b'):
            length -= 2
        for inner in range(0, length, 1):
            inindex = 0
            player = body[inner].findAll('td')
            for play in player:
                if(inindex == 0):
                    player[inindex] = [play.find('span', {'class', 'abbr'}).contents[0], play.find(
                        'span', {'class', 'position'}).contents[0]]
                else:
                    player[inindex] = play.contents[0]
                inindex += 1
            body[index] = player
            index += 1
        if(cheak == 'b'):
            return body[:-2]
        else:
            return body

    # start player
    startthead = score_thead(scoretable.findAll('thead')[0].findAll('th'))
    startscroe = score_tbody(scoretable.findAll('tbody')[0].findAll('tr'), 's')
    # bench player
    benchthead = score_thead(scoretable.findAll('thead')[1].findAll('th'))
    benchscroe = score_tbody(scoretable.findAll('tbody')[1].findAll('tr'), 'b')

    return [startthead, startscroe, benchthead, benchscroe]


def gamebox(gameID):
    res = requests.get('http://www.espn.com/nba/boxscore?gameId=' + gameID)
    soup = BeautifulSoup(res.text, "lxml")

    home = get_wrapper(soup, 'col column-two gamepackage-home-wrap')
    away = get_wrapper(soup, 'col column-one gamepackage-away-wrap')

    homebox = [home[1], home[3]]
    awaybox = [away[1], away[3]]

    return [homebox, awaybox]
