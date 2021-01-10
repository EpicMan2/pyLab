import tweepy
import re
import sys

ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

# Setup access to API
def twitterConnect():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    return api

# Find the word
def findLongest(wordline):
	longword = ''
	longindex = 0
	for index, word in enumerate(wordline):
		if len(word) > len(longword):
			longword = word
			longindex = index
	del wordline[longindex]
	return longword

def findSmallest(wordline):
	smallword = '00'
	smallindex = 0
	for index, word in enumerate(wordline):
		if len(word) <= len(smallword):
			smallword = word
			smallindex = index
	del wordline[smallindex]
	return smallword

api = ''
try:
	api = twitterConnect()
except tweepy.TweepError as e: 
    print("Tweepy Error: {}".format(e))

print('Δώστε ένα account')
account = input()

user_tweets = ''
try:
	user_tweets = tweepy.Cursor(api.user_timeline, id=account, tweet_mode='extended').items(10)
except tweepy.TweepError as e: 
	print("Tweepy Error: {}".format(e))

longline = ''
try:
	for tweet in user_tweets:
		textline = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet.full_text)
		textline = re.sub(r'[^\s\w]', '', textline)
		textline = textline.replace('RT', '')
		longline += textline
		longline += '\n'
except tweepy.TweepError as e: 
	print("Tweepy Error: {}".format(e))

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), '')
longline_formatted = re.sub(r'\B\@\w+', '', longline.translate(non_bmp_map))
wordlistBig = str.split(longline_formatted)
wordlistSmall = str.split(longline_formatted)

print(longline)

for x in range(5):
	print(findLongest(wordlistBig))

for x in range(5):
	print(findSmallest(wordlistSmall))