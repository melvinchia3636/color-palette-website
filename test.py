import requests
from fake_useragent import UserAgent
import json

data = {
	'sortToken': 'T637477953741949798_Popular,N_3d39',
	'startRows': '0',
	'maxRows': '32', 
	'hasMoreRows': 'true',
	'sortPosition': '1',
}

s = requests.Session()

content = s.get('https://games.roblox.com/v1/games/sorts?gameSortsContext=HomeSorts').json()

json.dump(s.get('https://games.roblox.com/v1/games/list?sortToken='+content['sorts'][0]['token']+'&startRows=0&maxRows=1000&hasMoreRows=false&sortPosition=1&pageContext.pageId='+content["pageContext"]["pageId"]).json(), open('test.json', 'w'), indent=4)