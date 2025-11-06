import os

import dotenv
import requests


def main():
    print("My little brother listens to..")
    dotenv.load_dotenv()
    url = os.environ.get("LISTENBRAINZ_API_URL")
    response = requests.get(url)
    response.raise_for_status()
    json = response.json()
    item_list = []
    for listen in response.json()["payload"]["listens"]:
        item = listen["track_metadata"]["release_name"]
        if item not in item_list:
            item_list.append(item)
    for item in item_list:
        print(f"## {item}")


if __name__ == "__main__":
    main()
