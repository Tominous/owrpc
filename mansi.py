# mansi.py | maxicc's ANSI Colours
# https://www.github.com/maxicc

class colours():
    """
    Colour and prefix-related configurations.
    """
    blue = '\033[94m' # Info, blue
    green = '\033[92m' # Success, green
    orange = '\033[93m' # Warn, orange
    red = '\033[91m' # Fail, red
    reset = '\033[0m' # Reset
    grey = '\033[90m' # Grey

    warn = reset + orange + "[!] " + reset
    fail = reset + red + "[✘] " + reset
    info = reset + blue + "[~] " + reset
    ask = reset + grey + "[?] " + reset
    cmd = reset + orange + "[$] " + reset
    success = reset + green + "[✓] " + reset
    smile = reset + red + "[☺] " + reset
    blank = reset + grey + "[#] "

class nocolours():
    """
    Colour and prefix-related configurations for use when colours are disabled.
    """
    warn = "[!] "
    fail = "[✘] "
    info = "[~] "
    ask = "[?] "
    cmd = "[$] "
    success = "[✓] "
    smile = "[☺] "
    blank = "[#] "
