from flask import Flask
from lib.create_game_id import create_game_id
from game import Game
import json

app = Flask(__name__)

# this is to keep track of all games, key is an id, value is the game...
games = {}


@app.route('/api/start')
def start():
    """
    this route creates a new game id, and creates a new game, passing in the ID
    """
    id = create_game_id()

    # create the new game, passing in the id
    game = Game(id)

    # add the game to the dictionary of games
    games[id] = game


if __name__ == '__main__':
    app.run()
