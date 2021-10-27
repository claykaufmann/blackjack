def create_game_id(games: dict) -> int:
    # collect all existing game ids
    keys = sorted(games.keys())

    # edge case if this is the first game
    if len(keys) <= 0:
        return 1

    last_key = keys[len(keys) - 1]

    # return the last one plus 1
    return last_key + 1
