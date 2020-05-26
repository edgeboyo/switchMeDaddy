import tweepy
from tweepy import OAuthHandler 

def clearcomment(s): # takes out comment and excess chars
    s = s.split('#')[0]
    while(s[len(s)-1] == ' ' or s[len(s)-1] == '\n'):
        s = s[:-1]
    return s

def wasIHere(api, tweet): # checks own tweet for tweets that replyt to this tweet
    l = 0
    for status in tweepy.Cursor(api.user_timeline, q="to:{}".format(tweet.user.name)).items():
        l = l + 1
        if hasattr(status, 'in_reply_to_status_id'):
              if (status.in_reply_to_status_id == tweet.id):
                return False
    print("This one went through!")
    return True

def findAndReply(cachedName): # find, reply to unseen tweets and get a list of links of new ones to be sent
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

    userTweets = api.user_timeline(screen_name = cachedName, count = 100, include_rts = True)

    userNintendoTweets = []

    for tweet in userTweets:
        if(tweet.source == 'Nintendo Switch Share' and wasIHere(api, tweet)):
            userNintendoTweets.append(tweet)

    userTweets = userNintendoTweets 

    imageUrls = []

    for tweet in userTweets:
        if 'media' in tweet.extended_entities:
            for image in tweet.extended_entities['media']:
                imageUrls.append(image['media_url'])
        api.update_status('@{} I got you! I\'ve sent your picture to your discord!'.format(tweet.user.screen_name), tweet.id)
    print("{} entries:\n{}".format(len(imageUrls), imageUrls))

    return imageUrls 
    

if __name__ == "__main__":
    findAndReply('SwitchMeDaddy1')