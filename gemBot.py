import praw
import time
import os
import getReply

r = praw.Reddit(user_agent = "GW2 reply bot - /u/rGW2bot")

# Leaving login() empty prompts the user for their username and password, more secure.
print("\nPlease log in:")
r.login()

operatingSubreddit = "test"
alertWords = ["!gemprice", "!gemprices", "!gemrate"]
pullLimit = 50
# pullGroups will track how many groups of comments have been pulled.
pullGroups = 0

print("\nCurrently parsing comments in /r/" + operatingSubreddit)

def runBot():
    global pullGroups

    subreddit = r.get_subreddit(operatingSubreddit)

    # Pull comments from subreddit:
    print("Pulling comments for group " + str(pullGroups) + "...")
    comments = subreddit.get_comments(limit=pullLimit)

    def commentParsing():

        # Loading the comment ID's that have already been replied to, prevents double-posting:
        if not os.path.isfile("replyIDs.txt"):
            print("replyIDs.txt not found, please create it!")
            commentsSeen = []
        else:
            with open("replyIDs.txt", "r") as c:
                commentsSeen = c.read()
                commentsSeen = commentsSeen.split("\n")
                commentsSeen = list(filter(None, commentsSeen))
        print(commentsSeen)

        global pullGroups
        print("Beginning parsing...")

        for comment in comments:
            # Set comment's text to lower case, making alertWordsrt word casing less strict:
            commentText = comment.body.lower()
            isAlertComment = any(string in commentText for string in alertWords)

            if comment.id not in commentsSeen and isAlertComment:
                print("    > Alert comment found! ID: " + comment.id + "\n    > Comment text: " + commentText + "\n    > Replying now...")

                # Anti-crash code to prevent the bot from stopping in-case gemBot.py cannot get a response (if GW2Spidy.com is down):
                try:
                    comment.reply(getReply.gemComment())
                    print("    > Reply sent! (ID: " + comment.id + ")")
                    print("    > Comment added to commentsSeen (ID: " + comment.id + ")")
                    with open("replyIDs.txt", "a") as c:
                        c.write(comment.id + "\n")
                except:
                    print("    > No response from gemBot.py. Perhaps GW2Spidy is down?")
                    print("    > Comment was not added to commentsSeen (ID: " + comment.id + ") \n")
                    print("    > Beginning pull of next group of comments now... \n")
        pullGroups += 1

    commentParsing()
    print("Parsed a total of " + str(pullGroups * pullLimit) + " comments so far. \n")

while True:
    runBot()
    time.sleep(10)