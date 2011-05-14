import twitter

import optparse
import sys

def print_safe(string):
    """
    Format a string for safe printing
    """
    return string.encode('cp437', 'xmlcharrefreplace')

def print_tweet(tweet):
    """
    Format and print `tweet`.
    """
    print "@" + print_safe( tweet.GetUser().GetScreenName() ) +  \
    ": " + print_safe(tweet.GetText())

def search(search_term):
    """
    Print recent tweets containing `search_term`.
    """
    api = twitter.Api()
    tweets = api.GetSearch(search_term)
    for tweet in tweets:
        print_tweet(tweet)

def trending_topics():
    """
    Print the currently trending topics.
    """
    api = twitter.Api()
    trending_topics = api.GetTrendsCurrent()
    for topic in trending_topics:
        print print_safe(topic.name)

def user_tweets(username):
    """
    Print recent tweets by `username`.
    """
    api = twitter.Api()
    user_tweets = api.GetUserTimeline(screen_name=username)
    for tweet in user_tweets:
        print_tweet(tweet)

def trending_tweets():
    """
    Print tweets for all the trending topics.
    """
    api = twitter.Api()

    trending_topics = api.GetTrendsCurrent()
    tweets = []
    # To add some variety, let's round-robin through the trending
    # topics, displaying a tweet from each until we run out of tweets.
    for topic in trending_topics:
        tweets.append((topic, api.GetSearch(topic.name)))

    while True:
        for topic, topic_tweets in tweets:
            if topic_tweets:
                print_tweet(topic_tweets.pop())
            else:
                return

def main(args):
    parser = optparse.OptionParser("""Usage: %prog [-s <search term> | -t | -u <username>]""")

    parser.add_option("-s", "--search",
                      type="string",
                      action="store",
                      dest="search_term",
                      default=None,
                      help="Display tweets containing a particular string.")
    parser.add_option("-t", "--trending-topics",
                      action="store_true",
                      dest="trending_topics",
                      default=False,
                      help="Display the trending topics.")
    parser.add_option("-u", "--user",
                      type="string",
                      action="store",
                      dest="username",
                      default=None,
                      help="Display tweets for a particular public user.")
    parser.add_option("-w", "--trending-tweets",
                      action="store_true",
                      dest="trending_tweets",
                      default=None,
                      help="Display the tweets from trending topics.")

    (opts, args) = parser.parse_args(args)

    if opts.search_term:
        search(opts.search_term)
    elif opts.trending_topics:
        trending_topics()
    elif opts.username:
        user_tweets(opts.username)
    elif opts.trending_tweets:
        trending_tweets()

if __name__ == "__main__":
    main(sys.argv[1:])
