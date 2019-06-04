# owrpc

*some cool badges will go here soon*

###### Overwatch + Discord Rich Presence = <3

![A demonstration of the rich presence in action](https://i.imgur.com/MnPOmzD.png)

![Another demonstration of the rich presence](https://i.imgur.com/v1l6Flx.png)

## About

This is a Python script that will allow you to set your own Discord Rich Presence for Blizzard Entertainment's *Overwatch*.

Currently, Blizzard seems too focused on Battle.net as a platform (zzz) to implement Rich Presence for Overwatch, so this is one way of getting it. If you prefer a more automatic method, you can use [OverTrack](https://www.overtrack.gg), created by [@synap5e](https://www.github.com/synap5e) - it's wonderful!

## Dependencies

- [x] Python 3 *(programmed using 3.6.5)*

- [x] [pypresence](https://github.com/qwertyquerty/pypresence) - install via pip using `pip install pypresence`

- [ ] A functioning brain

- [x] Some patience

## How to use

1. Clone the repo with `git clone https://github.com/maxicc/overwatch-rpc.git` or download the ZIP version from the top of this page.
* *(sidenote: please do not change anything in the config file - you don't need your own Discord client ID or anything!)*
2. Open up a Terminal window in the directory you cloned or downloaded this repo to.
3. Run `pip install pypresence` if you don't already have it installed.
4. Make sure Discord is running, then run `python owrpcMain.py`. You should be greeted by the program!
5. That's it, you're done! 🎉 Now, run `!help` to see what commands are available. Or just, you know, look below.

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
