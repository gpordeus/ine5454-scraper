import requests
import json
from bs4 import BeautifulSoup

class Game:
    def __init__(self):
        self.name = None
        self.price = None
        self.genre = []
        self.tags = []
        self.rating = None
        self.reviews = []
        self.description = None
        self.requirements = None
        self.developers = []
        self.publisher = None
        self.release_date = None
        self.languages = []


uris = [
    'https://store.steampowered.com/app/292030/The_Witcher_3_Wild_Hunt/',
    'https://store.steampowered.com/app/814380/Sekiro_Shadows_Die_Twice__GOTY_Edition/',
    'https://store.steampowered.com/app/310950/Street_Fighter_V'
]

games = []
for uri in uris:
    soup = BeautifulSoup(requests.get(uri).text, 'html.parser')
    game = Game()

    selection = soup.select('div#appHubAppName')
    game.name = selection[0].text.strip()

    selection = soup.select('div.game_purchase_price.price')
    price = selection[0].text.strip()
    price = price.split()
    game.price = float(price[1].replace(',','.'))

    selection = soup.select('div#genresAndManufacturer')
    game.genre.append(selection[0].select('a')[0].text.strip())

    selection = soup.select('div.glance_tags.popular_tags a.app_tag')
    for s in selection:
        game.tags.append(s.text.strip())

    selection = soup.select('div#developers_list a')
    for s in selection:
        game.developers.append(s.text.strip())

    selection = soup.select('div#languageTable td.ellipsis')
    for s in selection:
        game.languages.append(s.text.strip())


    games.append(game)



for g in games:
    print(json.dumps(g.__dict__))
