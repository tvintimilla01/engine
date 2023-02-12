def formatter(game):
    
    game = game.translate(str.maketrans({':': '', ' ': '-'}))

    return game.lower()


print(formatter("The Elder Scrolls V: Skyrim"))
