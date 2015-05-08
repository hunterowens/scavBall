import requests

url = "http://gd2.mlb.com/components/game/mlb/year_2015/month_05/day_07/master_scoreboard.json"

r = requests.get(url)
data = r.json()
games = data['data']['games']['game']

last_game = games.pop()

def findGame():
    """
    finds the game out of the game list, returns it
    """
    return last_game

game = findGame()

def runners():
    """
    Turns on the light for the runners
    """
    pass

def atBat():
    pass


