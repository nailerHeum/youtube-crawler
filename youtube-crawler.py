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
    raw_response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos', params=params_setting)
    status_code = raw_response.status_code
    response = raw_response.json()
    if status_code != 200:
        print(status_code)
        print("request failed, exiting")
        return
    print(f"""
    kind            {response['kind']}
    pageInfo        {response['pageInfo']}
    nextPageToken   {response['nextPageToken']}

<<<< VIDEO INFO >>>>
    """)
    print(f"video keys : {response['items'][0]['snippet'].keys()}")
    for video in response['items']:
        print(f"""
IDENTIFIER :    {video['id']}

TITLE :         {video['snippet']['title']}

DESCRIPTION :   {video['snippet']['description']}

CHANNEL :       {video['snippet']['channelTitle']}

      """)


if __name__ == '__main__':
    main()
