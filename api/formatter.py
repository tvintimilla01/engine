def formatter(game):

    game = "".join([i.replace(i,"") if i == ":" else i for i in game])
    game = "".join([i.replace(i,"-") if i == " " else i for i in game])

    return game.lower()


print(formatter("The Elder Scrolls V: Skyrim"))