import requests

url = "http://gd2.mlb.com/components/game/mlb/year_2015/month_05/day_07/master_scoreboard.json"

r = requests.get(url)
data = r.json()
games = data['data']['games']['game']

