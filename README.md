# gemBot

What does it do?
----------------
Written entirely in Python 3, this bot will pull comments from the subreddit [/r/GuildWars2](http://www.reddit.com/r/guildwars2), check if they contain given alert words, and then respond with data taken from the GW2Spidy API. For example, if one were to comment "!gemprice 500" the bot will reply with the current buying price of 500 gems, the current selling price of gems 500, and the cost to buy 500 gems with USD within the game of Guild Wars 2. The sell/buy price returned in the reply are taken from the [GW2Spidy API](https://github.com/rubensayshi/gw2spidy/wiki/API-v0.9), which is pulled from the popular website [GW2Spidy](http://www.gw2spidy.com/).

You can view the current buy and sell prices of gems on the GW2Spidy website [here](http://www.gw2spidy.com/gem).

Features:
---------

- Comments that have been replied to have their IDs stored in the `replyIDs.txt` file, so that the bot will not reply twice to a comment containing a certain keyword, even after a restart.
- A quantity limit makes sure that requests cannot be made with the quantity being over 9999. In this case, the quantity is just set to 9999.
- If no quantity is set, or non-numeric numbers are present after "!gemprice", the bot will simply show the data for a quantity of 100 gems.
- Anti-crash code to ensure that the bot will not crash if GW2Spidy is down, or Reddit is down. This allows for the bot to be run externally on some external machine without worrying about crashes.
- Easy to modify and lightweight. 

Example use:
------------
Here a user posted a comment containing the alert words "!gemprice 800" and the bot responded accordingly:
<p align="center">
  <img src="http://i.imgur.com/9Uk5mWq.png" alt="gemBot example of use."/>
</p>

Requirements
------------

- [PRAW](https://praw.readthedocs.org/en/v2.1.21/): The Python Reddit API Wrapper
- A Python 3 wrapper for the GW2Spidy API. In this case, you can use my wrapper, [pygw2spidy](https://github.com/snowspirit/pygw2spidy). Just include it in the project folder.

Note:
-----
GemBot is configured to parse the subreddit /r/test, to change it to your desired subreddit simply change the line with `operatingSubreddit = "test"` to whichever subreddit you desire.

License:
--------
Provided under the [MIT Open Source License](http://opensource.org/licenses/MIT), you are free to use this project and edit it to your own needs so long as you keep the following copyright notice within the project. Also, I am not responsible if this bot is modified to cause harm.

    Copyright (c) 2015 Luna Foster (github dot com slash snowspirit)
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
