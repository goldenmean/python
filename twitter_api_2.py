import tweepy
from tweepy import Client, OAuth2AppHandler
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


# Initialize OAuth handler
auth = OAuth2AppHandler(
    client_id=X_API_KEY,
    client_secret=X_API_SECRET,
    access_token=X_ACCESS_TOKEN
)

# Initialize API client
client = Client(auth=auth)

try:
    # Send tweet
    response = client.create_tweet(text="Hello, Twitter!")
    print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
except tweepy.TweepError as e:
    print(f"Error occurred while posting the tweet: {str(e)}")