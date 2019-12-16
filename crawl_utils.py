import requests
import json
with open('youtube_key.json', "r") as json_str:
    YOUTUBE_API_KEY = json.load(json_str)["YOUTUBE_API_KEY"]
END_POINT = "https://www.googleapis.com/youtube/v3/videos"
DEFAULT_PARAMS = {
    'key': YOUTUBE_API_KEY,
    'part': 'snippet',
    'chart': 'mostPopular',
    'regionCode': 'KR'
}


def set_params(pageToken=None):
    """
    SETTING PARAMETERS
    """
    params = DEFAULT_PARAMS
    if pageToken:
        params['pageToken'] = pageToken
    return params


def is_invalid_res(raw_res):
    if raw_res.status_code != 200:
        print(f"""
        {raw_res.status_code}
        request failed, exiting
        """)
        return True
    return False


def get_raw_res(params=None):
    return requests.get(END_POINT, params=params)


def print_res_infos(response):
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
