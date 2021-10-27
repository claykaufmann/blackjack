from flask import Flask, request
from lib.create_game_id import create_game_id
from game import Game
import time

app = Flask(__name__)

# this is to keep track of all games, key is an id, value is the game...
games = {}


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/api/start')
def start():
    """
    this route creates a new game id, and creates a new game, passing in the ID
    """
    id = create_game_id(games)

    # create the new game, passing in the id
    game = Game(id)

    # add the game to the dictionary of games
    games[id] = game

    # get initial deal
    game.initial_deal()

    # return game id, and cards to JS
    player_cards = game.player.cards
    dealer_cards = game.dealer.cards

    return {
        'player': {
            'cards': player_cards
        },
        'dealer': {
            'cards': dealer_cards
        },
        'game_id': id
    }


@app.route('/api/game_action/<game_id>')
def game_action(game_id):
    if game_id not in games.keys():
        return "fatal error"

    # get action from req
    data = request.get_json()

    # get ID from req

    # call necessary functions
    games[game_id].game_flow(data.action)

    # return relevant information

    return "hello world"


if __name__ == '__main__':
    app.run()
