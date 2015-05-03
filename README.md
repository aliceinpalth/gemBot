# gemBot

What does it do?
----------------
Written entirely in Python 3, this bot will pull comments from the subreddit [/r/GuildWars2](http://www.reddit.com/r/guildwars2), check if they contain given alert words, and then respond with data taken from the GW2Spidy API. In this case, if one were to comment "!gemprice", "!gemprices", or "!gemrate", the bot will reply with the current buying price of gems and the current selling price of gems within the game of Guild Wars 2. The sell/buy price returned in the reply are taken from the [GW2Spidy API](https://github.com/rubensayshi/gw2spidy/wiki/API-v0.9), which is pulled from the popular website [GW2Spidy](http://www.gw2spidy.com/).

Requirements
------------

- [PRAW](https://praw.readthedocs.org/en/v2.1.21/): The Python Reddit API Wrapper
- A Python3 wrapper for the GW2Spidy API. In this case, you can use my wrapper, [pygw2spidy](https://github.com/snowspirit/pygw2spidy).

Features:
---------

- Comments that have been replied to have their IDs stored in the `replyIDs.txt` file, so that the bot will not reply twice to a comment containing a certain keyword, even after a restart.
- Easy to modify.

Note:
-----
GemBot is configured to parse the subreddit /r/test, to change it to your desired subreddit simply change the line with `operatingSubreddit = "test"` to whichever subreddit you desire.
