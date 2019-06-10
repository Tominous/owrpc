# owrpcconfig.py | Overwatch RPC Client Configuration
# https://www.github.com/maxicc/owrpc

class configs():
    """
    Configurations relating to the program itself.
    Should not be changed by users.
    """

    client = 583356928688783369
    ver = "1.0.2"

class maps():
    """
    Map-related configurations. Must be updated as new maps come out!
    Should not be changed by users.

    The formatting for modes is as follows:
    "short-mode-name": ["Full Mode Name","mapset"]

    The formatting for maps is as follows:
    "short-map-name": ["Full Map Name","type","discord-key"]
    """
    modes = {
        "competitive": ["Competitive","standard"],
        "quick": ["Quick Play","standard"],
        "arcade": ["Arcade","any"],
        "custom": ["Custom Game","any"]
    }

    standard = {
        "hanamura": ["Hanamura","Assault","hanamura"],
        "horizon": ["Horizon Lunar Colony","Assault","horizon"],
        "paris": ["Paris","Assault","paris"],
        "anubis": ["Temple of Anubis","Assault","temple-of-anubis"],
        "volskaya": ["Volskaya Industries","Assault","volskaya"],
        "dorado": ["Dorado","Escort","dorado"],
        "havana": ["Havana","Escort","havana"],
        "junkertown": ["Junkertown","Escort","junkertown"],
        "rialto": ["Rialto","Escort","rialto"],
        "route66": ["Route 66","Escort","route-66"],
        "gibraltar": ["Watchpoint: Gibraltar","Escort","watchpoint-gibraltar"],
        "blizzard": ["Blizzard World","Hybrid","blizzard-world"],
        "eichenwalde": ["Eichenwalde","Hybrid","eichenwalde"],
        "hollywood": ["Hollywood","Hybrid","hollywood"],
        "kingsrow": ["King's Row","Hybrid","kings-row"],
        "numbani": ["Numbani","Hybrid","numbani"],
        "busan": ["Busan","Control","busan"],
        "ilios": ["Ilios","Control","ilios"],
        "lijiang": ["Lijiang Tower","Control","lijiang"],
        "nepal": ["Nepal","Control","nepal"],
        "oasis": ["Oasis","Control","oasis"]
    }

    arcade = {
        "blackforest": ["Black Forest","Arcade","black-forest"],
        "castillo": ["Castillo","Arcade","castillo"],
        "antarctica": ["Ecopoint: Antarctica","Arcade","ecopoint-antarctica"],
        "necropolis": ["Necropolis","Arcade","necropolis"],
        "chateau": ["Château Guillard","Arcade","chateau"],
        "petra": ["Petra","Arcade","petra"],
        "ayutthaya": ["Ayutthaya","Arcade","ayutthaya"],
        "seasonal": ["Overwatch Event","Seasonal","overwatch"]
    }
