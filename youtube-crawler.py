import json
import requests


def main():
    """
    GETTING YOUTUBE's TRENDING VIDEOS
    """
    with open('./youtube_key.json', "r") as json_str:
        YOUTUBE_API_KEY = json.load(json_str)["YOUTUBE_API_KEY"]
    params_setting = {
        'key': YOUTUBE_API_KEY,
        'part': 'snippet',
        'chart': 'mostPopular',
        'regionCode': 'KR'
    }
    response = requests.get('https://www.googleapis.com/youtube/v3/videos',
                            params=params_setting)
    print(response.json())


if __name__ == '__main__':
    main()
