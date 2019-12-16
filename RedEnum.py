from optparse import OptionParser
import praw


def main():
    options = handleCommandArgs()
    reddit = redditAuth()
    if reddit == 0:
        return

    account = reddit.redditor(options.user)  # get account overview
    displaySubredditStats(options, account)


############################
# This function takes in the parsed command line arguments and a redditor instance
# of the user to enumerate.
# Currently the function only displays a formatted chart of the subreddits commented
# in and the number of times.
############################

def displaySubredditStats(options, account):
    comment_subs = dict()
    for comment in account.comments.new(limit=None):  # iterating through the comments in the account

        if comment.subreddit not in comment_subs:  # if the subreddit has not already been commented in, add it to the dictionary
            comment_subs[comment.subreddit] = 1
        else:
            comment_subs[comment.subreddit] += 1  # increment the count for the subreddit by 1

    print('Subreddit\t\t\t\tCount\n' + '#' * 29)
    for sub in comment_subs.items():
        print("{a:25} {b:4}".format(a=str(sub[0]), b=str(sub[1])), '\n' + "- " * 14)  # print formatted output


def redditAuth():
    reddit = praw.Reddit("RedEnum", user_agent="script by /u/RedEnum_bot")  # authorize the bot
    if reddit.read_only:
        return reddit
    else:
        print("Error: Could not authenticate to Reddit")
        return 0


############################
# This function is responsible for handling the command line options of the program.
# Returns a list of the options passed by the user.
############################
def handleCommandArgs():
    parser = OptionParser()
    parser.add_option("-u", "--user", dest="user", help="The reddit account name to be enumerated")
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False,
                      help="Turn on verbose mode to give more output")
    (options, args) = parser.parse_args()
    return options


if __name__ == '__main__':
    main()
