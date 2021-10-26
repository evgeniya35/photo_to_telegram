from os import environ
import requests
import json

from load_photo import loadphoto


def fetch_spacex_last_launch(url):
    response = requests.get(url=url)
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]


if __name__ == "__main__":
    url = "https://api.spacexdata.com/v5/launches/5eb87d46ffd86e000604b388"
    photos = fetch_spacex_last_launch(url=url)
    for photo_num, url in enumerate(photos):
        loadphoto(
            url=url,
            folder="images",
            photo=f"spacex{photo_num}.jpg"
            )
