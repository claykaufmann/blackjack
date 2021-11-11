from typing import Dict
from flask import Flask, request
from lib.create_game_id import create_game_id
from game import Game
import logging

app = Flask(__name__)

# this is to keep track of all games, key is an id, value is the game...
games: Dict[int, Game] = {}


@app.route('/api/start')
def start():
    """
    this route creates a new game id, and creates a new game, passing in the ID
    """
    id = create_game_id(games)

    games[id] = id

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
            # TODO this needs to be turned into json by using the to_json card method
            "cards": game.player.cards_as_json()
        },
        'dealer': {
            'cards': game.dealer.cards_as_json()
        },
        'game_id': id
    }


# @app.route('/api/test_game/<game_id>', methods=['GET', 'POST'])
# def test_game(game_id):
#     if int(game_id) not in games.keys():
#         return {
#             'error': "Game ID not found"
#         }

#     data = request.get_json()

#     app.logger.info(data)

#     return {
#         "body": "hello world"
#     }


@app.route('/api/game_action/<game_id>')
def game_action(game_id):
    if int(game_id) not in games.keys():
        return "fatal error"

    # get action json data
    data = request.get_json()

    # call necessary functions
    # game_over true if game is over
    game_over = games[game_id].action_input(data.action)

    if game_over == True:
        # delete game here
        pass

    # return newly dealt cards
    return {
        "cards": games[game_id].get_cards(),
        "gameStatus": game_over
    }

@app.route('/api/make-bet')
def make_bet():
    data = request.get_json()

    bet = data.bet

    # make call to game bet functionality here

@app.route('/test')
def test():
    game = Game(1)

    game.initial_deal()

    game_over = game.action_input("hit")

    return {
        "cards": game.get_cards(),
        "gameStatus": game_over
    }


if __name__ == '__main__':
    app.run()
