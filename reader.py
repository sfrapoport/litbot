from __future__ import division
import os, random, re
from collections import defaultdict, Counter
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from gutenberg.query import get_metadata

regex = r"[\w']+|[\.]"

def generate_tweets(gutenberg_id, total=24):
    document = []
    text = strip_headers(load_etext(gutenberg_id)).strip()
    lines = text.split('\n')    
    print get_metadata('title', gutenberg_id)
    for line in lines:
        words = re.findall(regex, line)
        document.extend(words)

    trigrams = zip(document, document[1:], document[2:])
    trigram_transitions = defaultdict(list)
    starts = []

    for prev, current, next in trigrams:
            if prev == ".":
                    starts.append(current)
            trigram_transitions[(prev, current)].append(next)

    def generate_using_trigrams():
            current = random.choice(starts)
            prev = "."
            result = [current]
            while True:
                    next_word_candidates = trigram_transitions[(prev, current)]
                    next_word = random.choice(next_word_candidates)
                    prev, current = current, next_word
                    if current != ".":
                        result.append(current)
                    else:
                        return " ".join(result) + current
    tweets = [];
    while len(tweets) < total:
        tweet = generate_using_trigrams()
        if len(tweet) <= 140:
            tweets.append(tweet)
    return tweets

print generate_tweets(16328)
