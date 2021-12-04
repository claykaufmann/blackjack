def find_gap(games):
    return [x for x in range(games[0], games[-1]+1) if x not in games]

def create_game_id(games: dict) -> int:
    # collect all existing game ids
    keys = sorted(games.keys())

    # edge case if this is the first game
    if len(keys) <= 0:
        return 1
    
    id_gaps = find_gap(keys)

    # if there is at least one entry, the first number is the lowest, we want to
    # use this one
    if len(id_gaps) > 0:
        return id_gaps[0]

    last_key = keys[len(keys) - 1]

    # return the last one plus 1
    return last_key + 1
