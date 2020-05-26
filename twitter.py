import tweepy
from tweepy import OAuthHandler 

def clearcomment(s): #just for comments
    s = s.split('#')[0]
    while(s[len(s)-1] == ' ' or s[len(s)-1] == '\n'):
        s = s[:-1]
    return s

def wasIHere(api, tweet):
    l = 0
    for status in tweepy.Cursor(api.user_timeline, q="to:{}".format(tweet.user.name)).items():
        l = l + 1
        if hasattr(status, 'in_reply_to_status_id_str'):
              if (tweet.in_reply_to_status_id_str == tweet.id):
                return False
    print(l)
    return True

def findAndReply():
    with open("twitter.token") as f:
        consumer_key = clearcomment(f.readline())
        consumer_secret = clearcomment(f.readline())
        access_key = clearcomment(f.readline())
        access_secret = clearcomment(f.readline())


    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)

    pp = []

    for i in tweepy.Cursor(api.user_timeline).items():
        pp.append(i)

    print(len(pp))

    userTweets = api.user_timeline(screen_name = 'SwitchMeDaddy1', count = 100, include_rts = True)

    userNintendoTweets = []

    for tweet in userTweets:
        if(tweet.source == 'Nintendo Switch Share' and wasIHere(api, tweet)):
            userNintendoTweets.append(tweet)

    userTweets = userNintendoTweets 

    print(len(userTweets))

    for tweet in userTweets:
        api.update_status('@{} I got you! I\'ve sent your picture to your discord!'.format(tweet.user.screen_name), tweet.id)

if __name__ == "__main__":
	findAndReply()