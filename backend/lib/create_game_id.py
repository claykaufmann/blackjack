from typing import Dict


def create_game_id(games: Dict):
    # collect all existing game ids
    last_id = 0

    keys = sorted(games.keys())

    last_key = keys[len(keys) - 1]

    # return the last one plus 1
    return last_key + 1
