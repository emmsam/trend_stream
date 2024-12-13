import requests
from config import TWITTER_BEARER_TOKEN

def fetch_trending_hashtags():
    url = "https://api.twitter.com/2/tweets/sample/stream"
    headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}

    try:
        response = requests.get(url, headers=headers, stream=True)
        for line in response.iter_lines():
            if line:
                print(line)  # Replace with logic to parse and save
    except Exception as e:
        print(f"Error fetching hashtags: {e}")

if __name__ == "__main__":
    fetch_trending_hashtags()
