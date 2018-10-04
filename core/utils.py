import importlib
import os


def is_player(mod):
    try:
        assert hasattr(mod, 'AUTHOR')
        assert hasattr(mod, 'NAME')
        assert hasattr(mod, 'Player')
        assert hasattr(mod.Player, 'play')
        return True

    except AssertionError as e:
        return False


def name2std(name):
    return name.lower().replace("-", "_").replace(" ", "_")


def discover_players():
    names = {}

    for folder in os.scandir('players'):
        try:
            mod = importlib.import_module('players.{}.player'.format(folder.name))
            if is_player(mod):
                name = name2std(mod.NAME)

                if name in names:
                    print("Colliding name {0}, between {1} and {2}".format(name, mod.AUTHOR, names[name].AUTHOR))
                else:
                    names[name] = mod
        except ModuleNotFoundError:
            pass

    return names
