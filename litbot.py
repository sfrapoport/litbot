import sys, os, random, re, time
# from twython import Twython
from reader import generate_tweets
# api_key, api_secret, access_token, token_secret = sys.argv[1:]
# twitter = Twython(api_key, api_secret, access_token, token_secret)

booknumbers = []
writefile = open('./gutenbergtweets.txt', 'w')

for line in open('./gutenbergids.txt', 'r'):
    if (line.strip('\n')):
        booknumbers.append(int(line.strip('\n')))

def post_tweet(tweet):
    print tweet
    writefile.write(tweet + '\n')
    # twitter.update_status(status=litbot_says)

while True:
    num = booknumbers.pop()
    tweets = generate_tweets(num)
    writefile.write('Book #' + str(num) + '\n')
    while len(tweets) > 0:
        litbot_says = tweets.pop()
        post_tweet(litbot_says)


