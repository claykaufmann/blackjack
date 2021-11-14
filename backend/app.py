from typing import Dict
from flask import Flask, request
from lib.create_game_id import create_game_id
from game import Game
import logging

app = Flask(__name__)

# this is to keep track of all games, key is an id, value is the game...
games: Dict[int, Game] = {}


@app.route('/api/start', methods = ['GET'])
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

    return {
        'player': {
            "cards": game.player.cards_as_json(),
            "value": game.player.value
        },
        'dealer': {
            'cards': game.dealer.cards_as_json(),
            "value": game.dealer.value
        },
        'game_id': id
    }


@app.route('/api/game_action/<game_id>', methods = ['GET', 'POST'])
def game_action(game_id):
    game_id = int(game_id)
    if game_id not in games.keys():
        return "fatal error"

    # get action json data
    data = request.get_json()

    game = games[game_id]

    # call necessary functions
    # game_over true if game is over
    game_over = game.action_input(data['action'])

    if game_over == True:
        # delete game here
        pass

    # return newly dealt cards
    return {
        'player': {
            "cards": game.player.cards_as_json(),
            "value": game.player.value
        },
        'dealer': {
            'cards': game.dealer.cards_as_json(),
            "value": game.dealer.value
        },
    }

@app.route('/api/make-bet')
def make_bet():
    data = request.get_json()

    bet = data.bet

    # make call to game bet functionality here



if __name__ == '__main__':
    app.run()
