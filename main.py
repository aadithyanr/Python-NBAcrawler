import get_game
import get_gamebox
import get_playbyplay
import json


class GameBox:
    home = ''
    away = ''


class GameMatch:
    HomeTeam = ''
    AwayTeam = ''
    GameStatus = ''


gameID = '401071198'
gameinfo = get_game.get_game(gameID)
gamebox = get_gamebox.gamebox(gameID)
gameplaybyplay = get_playbyplay.playbyplay(gameID, (len(gameinfo[2][0])-2))


# game scroe
Game = GameMatch()
Game.AwayTeam = gameinfo[0]
Game.HomeTeam = gameinfo[1]
Game.GameStatus = gameinfo[2]

# game box
GmaeBox = GameBox()
GameBox.home = gamebox[0]
GameBox.away = gamebox[1]

# save data
Gamescorejson = {}
Gamescorejson['AwayTeam'] = Game.AwayTeam
Gamescorejson['HomeTeam'] = Game.HomeTeam
Gamescorejson['GameStatus'] = Game.GameStatus
with open('Gamescore.json', 'w') as outfile:
    json.dump(Gamescorejson, outfile)


Gameboxjson = {}
Gameboxjson['Away'] = GameBox.away
Gameboxjson['Home'] = GameBox.home
with open('Gamebox.json', 'w') as outfile:
    json.dump(Gameboxjson, outfile)

Gameplayjson = {}
Gameplayjson['PlaybyPlay'] = gameplaybyplay
with open('Gameplay.json', 'w') as outfile:
    json.dump(Gameplayjson, outfile)