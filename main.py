import json
from os import getenv
import random
import requests
import tweepy
import schedule
import time
from typing import NoReturn, Optional, List
from dotenv import load_dotenv
from text_to_tweets import tweet_splitter

# Load environment variables
load_dotenv()
API_KEY = getenv("API_KEY")
API_SECRET_KEY = getenv("API_SECRET_KEY")
ACCESS_TOKEN = getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = getenv("BEARER_TOKEN")  # Required for Twitter API v2

# Authenticate to Twitter API v2
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
)

def send_tweet(tweet_content: str, reply_to_id: Optional[str] = None) -> Optional[str]:
    """Send a tweet with optional threading."""
    try:
        response = client.create_tweet(
            text=tweet_content,
            in_reply_to_tweet_id=reply_to_id if reply_to_id else None
        )
        tweet_id = response.data["id"]  # type: ignore
        print(f"Tweet sent successfully! Tweet ID: {tweet_id}")
        return tweet_id
    except tweepy.TweepyException as error:
        print(f"Error sending tweet: {error}")
        return None

def get_random_aya() -> List[str]:
    """Fetch a random Aya and its translation."""
    response = []
    aya = random.randint(1, 6237)
    api_response = requests.get(f"https://api.alquran.cloud/v1/ayah/{aya}/editions/quran-uthmani,fa.gharaati")
    data = api_response.json()

    for entry in data["data"]:
        aya_text = entry["text"]
        translation_text = entry.get("translation", {}).get("text", None)

        response.append(aya_text)
        if translation_text:
            response.append(translation_text)
    return response

def process_and_send_tweets() -> None:
    """Process the Aya and send tweets in a thread while handling large translations."""
    aya = get_random_aya()
    if not aya:
        print("Error: No Aya data retrieved.")
        return

    aya_text = aya[0]
    aya_translation = aya[1] if len(aya) > 1 else ""

    # Split Aya text and translation if necessary
    aya_text_parts = tweet_splitter(aya_text, counter=False)
    translation_parts = tweet_splitter(aya_translation, counter=False)

    previous_tweet_id = None

    # Send Aya text in chunks
    for i, part in enumerate(aya_text_parts):
        tweet_id = send_tweet(part, reply_to_id=previous_tweet_id)
        if tweet_id:
            previous_tweet_id = tweet_id

    # Send translation in chunks
    for i, part in enumerate(translation_parts):
        tweet_id = send_tweet(part, reply_to_id=previous_tweet_id)
        if tweet_id:
            previous_tweet_id = tweet_id

def schedule_daily_tweet() -> NoReturn:
    """Schedule the daily tweet."""
    schedule.every().day.at("20:00", tz="Asia/Tehran").do(process_and_send_tweets)

    while True:
        schedule.run_pending()
        time.sleep(60)  # wait one minute

if __name__ == "__main__":
    # Uncomment to schedule daily tweets
    schedule_daily_tweet()

    # Uncomment to test sending a tweet
    # process_and_send_tweets()
