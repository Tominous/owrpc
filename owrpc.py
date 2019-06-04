# owrpc.py | Overwatch RPC Client
# https://www.github.com/maxicc/owrpc

### - IMPORTS AND MAIN SETUP - ###

# Importing default Python modules
import time
import sys
import random
import os
from urllib.request import urlopen

try:
    # Importing custom project-specific modules
    from owrpcconfig import configs as x
    from owrpcconfig import maps as m
    # Importing pypresence
    from pypresence import Presence

# If imports didn't work...
except Exception as e:
    # Warn the user that the modules can't be imported then exit with error code 1
    print("[!] Error! Couldn't import a module. Did you download the dependencies?")
    print("[!] Check https://git.io/fju4R and make sure, then try running again.")
    sys.exit(1)

# If there is a file in this directory called ".nocol"
if os.path.exists(".nocol") == True:
    # Import a different version of the prefixes module that removes the ANSI colours
    from mansi import nocolours as c
else:
    # Import the normal colours module
    from mansi import colours as c

# Initialise the Discord Presence using pypresence then connect to Discord
dp = Presence(x.client)
dp.connect()

# Define the status class

class status():
    ingame = 0
    devmode = False
    currmap = ''
    currmode = ''
    presets = {
        "example":["details","state","overwatch","large_text","overwatch-dark","small_text"],
        "inmenus":["In Menus",None,"overwatch","Running OWRPC v" + x.ver + " by maxic#9999! Download it at https://git.io/fju4R",None,None],
        "inqueue":["In Queue",None,"overwatch","Running OWRPC v" + x.ver + " by maxic#9999! Download it at https://git.io/fju4R",None,None],
        "devmode":["Overwatch RPC Client","I'm being programmed!","maxic","Created by maxic#9999","overwatch","Under development!"]
    }

### - DEFINE FUNCTIONS - ###

def devMode():
    """
    This function will toggle the value of status.devmode when called.
    status.devmode starts as False.
    """
    status.devmode = not status.devmode

def setPresence(preset,details='',state='',large_image='',large_text='',small_image='',small_text=''):
    """
    This function sets the Discord Rich Presence.
    [details,state,large_image,large_text,small_image,small_text]
    """
    if preset != None:
        details = status.presets.get(preset)[0]
        state = status.presets.get(preset)[1]
        large_image = status.presets.get(preset)[2]
        large_text = status.presets.get(preset)[3]
        small_image = status.presets.get(preset)[4]
        small_text = status.presets.get(preset)[5]

    if status.devmode == True:
        details = "DEV MODE | " + details
    try:
        # Update the presence using the details provided when calling the function
        dp.update(details=details,state=state,large_image=large_image,large_text=large_text,small_image=small_image,small_text=small_text,start=int(time.time()))
    except Exception as e:
        # If there is an exception, inform the user then exit with error code 1
        print(c.fail + "Couldn't set your presence properly! :(")
        print(c.fail + "The error message from pypresence is: " + str(e))
        sys.exit(1)
    print(c.success + "Your presence has been updated! Discord may take a few seconds to update.")

# setPresence(None,details="Competitive: In Game",state="Hybrid on Hanamura",large_image="hanamura",large_text="Hanamura",small_image="diamond",small_text="3001 SR")

owquotes = ["Cheers, love! The cavalry's here!","¡Apagando las luces!","Old soldiers are hard to kill.","Clear skies, full hearts, can't lose.","Initiating the hack.","Your guardian angel.","It's in the refrigerator.","Look out world, Tracer's here!","Nerf this!","Fire in the hole!","Die, die, die!","Justice rains from above!","I will be your shield!","All systems buzzing!"]

print(c.smile + "Overwatch RPC Client v" + x.ver + " by github.com/maxicc (maxic#9999)")
onlver = urlopen("https://raw.githubusercontent.com/maxicc/owrpc/master/VERSION").read()
if float(x.ver) != float(onlver):
    print(c.warn + "You're out-of-date! The latest version on GitHub is " + str(onlver) + " and you're on " + x.ver + ".")
else:
    print(c.success + "You're up-to-date! The latest version on GitHub is " + str(onlver) + " and you're on " + x.ver + ".")
print(c.info + "Questions? Comments? Feature requests? Head to https://git.io/fju4R!")
print(c.blank + random.choice(owquotes))
setPresence("inmenus")

while True:
    pass
