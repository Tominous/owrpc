# owrpc

### You might also like [splat2rpc](https://git.io/splat2) - a Discord Rich Presence client for Nintendo's Splatoon 2!

![version](https://img.shields.io/badge/version-1.0.3-yellow.svg)
![python-versions](https://img.shields.io/badge/python-3.5%20|%203.6%20|%203.7-critical.svg)
![GPL-license](https://img.shields.io/badge/license-GPLv3-green.svg)
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

![owrpc Promo Hero](https://i.imgur.com/FfKMwXx.png)

###### Overwatch + Discord Rich Presence = <3

![A demonstration of the rich presence in action](https://i.imgur.com/MnPOmzD.png)

## About

This is a Python script that will allow you to set your own Discord Rich Presence for Blizzard Entertainment's *Overwatch*.

Currently, Blizzard seems too focused on Battle.net as a platform (zzz) to implement Rich Presence for Overwatch, so this is one way of getting it. If you prefer a more automatic method, you can use [OverTrack](https://www.overtrack.gg), created by [@synap5e](https://www.github.com/synap5e) - it's wonderful!

## Dependencies

- [x] Python 3 *(programmed using 3.6.5)*

- [x] [pypresence](https://github.com/qwertyquerty/pypresence) - install via pip using `pip install pypresence`

- [ ] A functioning brain

- [x] Discord ["Show game activity" enabled](https://i.imgur.com/VBAU5Cg.png)

- [x] Some patience

## How to use

1. Clone the repo with `git clone https://github.com/maxicc/owrpc.git` or download the ZIP version from the top of this page.
* *(sidenote: please do not change anything in the config file - you don't need your own Discord client ID or anything!)*
2. Open up a Terminal window in the directory you cloned or downloaded this repo to.
3. Run `pip install pypresence` if you don't already have it installed.
4. Make sure Discord is running, then run `python owrpc.py`. You should be greeted by the program!
5. That's it, you're done! 🎉 Now, run `!help` to see what commands are available. Or just, you know, look below.
6. *EXTRA STEP FOR WINDOWS USERS!* When testing this program on Windows, I noticed that the Windows Terminal doesn't, by default, display ANSI colours, instead it will just show the escape code (which makes the console display really ugly)! To get around this, create a file called `.nocol` in the same directory as `owrpc.py` - this will disable the colours. You could also use an alternate terminal - I know that [Terminus](https://eugeny.github.io/terminus/) works fine, as may others. Conversely, other platforms that struggle to display ANSI colours can disable them using the `.nocol` file.

## Commands
* !dev - Toggle development mode on or off.
* !help - View this help document.
* !quit - Close the program.

* !game - Start set up for a game.
* !custom - Set up a custom presence.
* !menus - Set your presence to In Menus.
* !queue [a/c/q] - Set your presence to In Queue for [a]rcade, [c]ompetitive or [q]uickplay.
* !clear - Remove your presence from Discord.

There are some added aliases in the code used for testing which you can use if you really want to be special/annoying.

## Future plans

I've got the whole summer off so I might as well try and improve my gaming experience through programming :^)

- [x] ~~Version 1.0! Actually make this and release it~~

- [ ] Computer vision-y type stuff so it can auto-detect maps and modes like OverTrack does

- [ ] ~~Clean up~~ and comment the code - this new version is a lot cleaner.

- [x] ~~Add provisions for future maps/events - seasonals like Winter Wonderland add new maps and modes every year~~ New modes can now be easily added, I'm going to work on making them easier to access now.
