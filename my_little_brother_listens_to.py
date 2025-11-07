import dotenv
import os
import requests


def main():
    print("My little brother listens to..")
    dotenv.load_dotenv()
    url = os.environ.get("LISTENBRAINZ_API_URL")
    response = requests.get(url)
    response.raise_for_status()
    json = response.json()
    item_list = {}
    for listen in response.json()["payload"]["listens"]:
        item = listen["track_metadata"]["additional_info"]["release_mbid"]
        if item not in item_list:
            item_list[item] = listen["track_metadata"]
    for item in item_list:
        print(f"+++")
        print(f"title = '{item_list[item]['release_name']} - {item_list[item]['artist_name']}'")
        print(f"date = YYYY-MM-DD #today")
        print(f"mediatype = 'record'")
        print(f"website = 'https://musicbrainz.org/release/{item}'")
        print(f"rating = ''")
        print(f"+++")


if __name__ == "__main__":
    main()
