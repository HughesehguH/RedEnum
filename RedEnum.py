from optparse import OptionParser
import praw

def main():
    options = handleCommandArgs()
    reddit = redditAuth()
    if reddit == 0:
        return
    
    account = reddit.redditor(options.user)
    for comment in account.comments.new(limit=None):
        print(comment.body,"\n")

    for submission in account.submissions.new():
      print("\n\nSubreddit: "+submission.subreddit.display_name, "\nTitle: "+submission.title)
    #print(account.comments)





def redditAuth():
    reddit = praw.Reddit("RedEnum", user_agent="script by /u/RedEnum_bot")
    if reddit.read_only == True:
        return reddit
    else:
        print("Error: Could not authenticate to Reddit")
        return 0


############################
#
# This function is responsible for handling the command line options of the program
# Returns a list of the options passed by the user
#
############################
def handleCommandArgs():
    parser = OptionParser()
    parser.add_option("-u", "--user", dest="user", help="The reddit account name to be enumerated")
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="Turn on verbose mode to give more output")
    (options, args) = parser.parse_args()
    return options


if __name__ == '__main__':
    main()