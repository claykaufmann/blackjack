def create_game_id(games: dict) -> int:
    # collect all existing game ids
    keys = sorted(games.keys())

    last_key = keys[len(keys) - 1]

    # return the last one plus 1
    return last_key + 1
