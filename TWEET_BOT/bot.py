import requests
import tweepy
import os  # Used for accessing environment variables

def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Programming")
    joke_data = response.json()
    if joke_data['type'] == 'single':
        return joke_data['joke']
    else:
        return f"{joke_data['setup']} ... {joke_data['delivery']}"

def lambda_handler(event, context):
    # Retrieve Twitter API credentials from environment variables
    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

    # Authenticate with Twitter using Tweepy
    client = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )

    # Get a joke
    joke = get_joke()

    # Tweet the joke
    response = client.create_tweet(text=joke)
    tweet_url = f"https://twitter.com/user/status/{response.data['id']}"
    print(tweet_url)

    return {
        'statusCode': 200,
        'body': tweet_url
    }
