import tweepy, time
from twitter_authentication import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

authentication = tweepy.OAuthHandler(API_KEY, API_SECRET)
authentication.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(authentication)

politician = "pmharper"

users = tweepy.Cursor(api.followers_ids, id=politician).items()

f = open("/github/followers/" + politician + ".txt", "a")

count = 0

while True:
	try:
		user = next(users)
		f.write(str(user) + ", ")
		count += 1
	except tweepy.TweepError:
		print "sleeping..."
		print count
		time.sleep(60*2)
		continue
	except StopIteration:
		break

f.close()
print count