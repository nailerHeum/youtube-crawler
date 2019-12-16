import json
import requests
from .crawl_utils import set_params, is_invalid_res
with open('./youtube_key.json', "r") as json_str:
    YOUTUBE_API_KEY = json.load(json_str)["YOUTUBE_API_KEY"]


class Video():
    def __init__(self, id, title, description, channel):
        self.id = id
        self.title = title
        self.description = description
        self.channel = channel


def print_infos(response):
    """
    RESPONSE INFORMATION
    """
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


def items_to_json(response, prev_result=[]):
    result = []
    result += prev_result
    return result + prev_result


def main():
    """
    GETTING YOUTUBE's TRENDING VIDEOS
    """
    params_setting = set_params()
    raw_response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos', params=params_setting)

    if is_invalid_res(raw_response):
        return

    response = raw_response.json()

    result = []
    for video in response['items']:
        result.append(Video(video['id'], video['snippet']['title'],
                            video['snippet']['description'], video['snippet']['channelTitle']))

    print([x.__dict__ for x in result])
    next_page_token = response['nextPageToken']
    while next_page_token:
        req_params = set_params(next_page_token)


if __name__ == '__main__':
    main()
