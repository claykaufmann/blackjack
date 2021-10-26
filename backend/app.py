from flask import Flask
from lib.create_game_id import create_game_id
from game import Game
import time
import json

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

    # return game id, and cards to JS
    return "hello world"


@app.route('/api/game_action')
def game_action(req):
    # get action from req

    # get ID from req

    # call necessary functions

    # return relevant information

    return "hello world"


if __name__ == '__main__':
    app.run()
