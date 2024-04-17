import os
import config
import requests

if __name__ == "__main__":
    config.setup_env()

    token = os.environ["GOOGLE_SEARCH_API_KEY"]

    URL = f"https://www.googleapis.com/customsearch/v1?key={token}&cx=c4285f29bbdb04ec5&q=indonesia"

    response = requests.get(URL)
    print(response.json())
