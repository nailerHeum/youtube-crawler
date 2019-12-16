def set_params(pageToken=None):
    """
    SETTING PARAMETERS
    """
    if pageToken:
        return {
            'key': YOUTUBE_API_KEY,
            'pageToken': pageToken
        }
    return {
        'key': YOUTUBE_API_KEY,
        'part': 'snippet',
        'chart': 'mostPopular',
        'regionCode': 'KR'
    }


def is_invalid_res(raw_res):
    if raw_res.status_code != 200:
        print(f"""
        {raw_res.status_code}
        request failed, exiting
        """)
        return True
    return False
