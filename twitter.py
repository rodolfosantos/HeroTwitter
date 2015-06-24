import tweepy 

# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

def tweet(status, photoPath):
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
 
    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)

    # Send the tweet with photo
    return api.update_with_media(photoPath, status=status)
