## Using Twitter/X APIs 

import tweepy
from textblob import TextBlob
from dotenv import load_dotenv
import os

load_dotenv()
#Load the twitter api key, secret, bearer token
X_API_KEY = os.getenv('X_API_KEY')
X_API_SECRET = os.getenv('X_API_SECRET')
X_BT_TOKEN = os.getenv('X_BEARER_TOKEN')

#For OAuth 1.1a based authentications
X_ACCESS_TOKEN= os.getenv('X_ACCESS_TOKEN')
X_ACCESS_TOKEN_SECRET= os.getenv('X_ACCESS_SECRET')

X_CLIENT_ID=os.getenv('X_CLIENT_ID')
X_CLIENT_SECRET=os.getenv('X_CLIENT_SECRET')

#authentication variable auth
client = tweepy.Client(
    bearer_token=X_BT_TOKEN,
    consumer_key=X_API_KEY,
    consumer_secret=X_API_SECRET,
    access_token=X_ACCESS_TOKEN,
    access_token_secret=X_ACCESS_TOKEN_SECRET
    
)

print("After authentication")

# Test the connection with a simple request
response = client.get_user(username="goldenmean")

if response.data:
    print("Client initialized successfully.")
else:
    print("Client initialized, but no data returned.")


'''
response = client.get_me()
print(response)

#Get followers of user goldenmean - no permission in Basic plan
followers_response = client.get_users_followers(id=response.data.id)
followers = followers_response.data
for follower in followers:
    print(f"Follower ID: {follower.id}, Name: {follower.name}, Username: {follower.username}")
'''
    
#auth = tweepy.OAuth2BearerHandler(X_BT_TOKEN)

#main variable
#api = tweepy.API(auth)

#Search tweets - no permission to search tweets in Basic plan
response = client.search_recent_tweets(query="Leetcode", max_results=10)

if response.data:
    for tweet in response.data:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
else:
    print("No tweets found.")



    
'''

## Authenticate using Oauth1.1
X_ACCESS_TOKEN = os.getenv('X_ACCESS_TOKEN')
X_ACCESS_TOKEN_SECRET = os.getenv('X_ACCESS_TOKEN_SECRET')

# Authenticate with the Twitter API v1.1
auth = tweepy.OAuth1UserHandler(X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

verified = api.verify_credentials()
print(f"Authentication successful. User ID: {verified.id}")

# Get trending topics for a specific location (WOEID for Worldwide is 1)
try:
    trends = api.get_place_trends(id=1)
    for trend in trends[0]['trends']:
        print(trend['name'])
except tweepy.TweepyException as e:
    print("Error fetching trends:", e)

'''