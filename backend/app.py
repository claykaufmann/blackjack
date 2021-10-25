from flask import Flask
import json

app = Flask(__name__)

# this is to keep track of all games, key is an id, value is the game...
games = {}


@app.route('start')
def start():
    """
    this route creates a new game id, and creates a new game, passing in the ID
    """
    id = create_game_id()

    # create the new game, passing in the id
    game = Game(id)

    # add the game to the dictionary of games
    games[id] = game


@app.route('/api/initial_deal')
def initial_deal(id):
    """
    takes in a game ID, which allows us to decipher which game...
    """
    player_card1 = Deck.deal()
    player_card2 = Deck.deal()

    json_card1 = player_card1.to_json()

    return "{'player': 'cards': [json_card1]"

    actions = req
    # do initial deal
    json = "hello"  # this becomes the JSON file

    return json


@app.route('/api/start')
def app():  # put application's code here
    deck = Deck()
    player = Player()

    # wait on information?

    return "hi"


@app.route('/api/shuffle')
def shuffle():
    deck.random()

    return json_string


@app.route('/api/deal_card')
def deal_card():

    json = json

    card = json.card


@app.route('api/player_actions')
def player_action():
    if "hit":
        card = Deck.deal()

    return json


if __name__ == '__main__':
    app.run()
