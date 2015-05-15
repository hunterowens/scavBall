import requests

url = "http://gd2.mlb.com/components/game/mlb/year_2015/month_05/day_08/master_scoreboard.json"

r = requests.get(url)
data = r.json()
games = data['data']['games']['game']

last_game = games.pop()
def _getLineup():
    """
    get the lineup
    """
    pass 

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
    runners = game['runners_on_base']
    if 'runner_on_1b' in runners:
        pass
        #light(firstBase Runne)
    if 'runner_on_2b' in runners:
        pass
        #light runn
    if 'runner_on_3b' in runners:
        pass

    pass

def atBat():
    batter= game['batter']
    print batter

def getOuts():
    pass

def getStrikes():
    pass

def getBalls():
    pass


if __name__ == '__main__':
    atBat()
