from crawl_utils import set_params, is_invalid_res, get_raw_res, print_res_infos


class Video():
    def __init__(self, id, title, description, channel):
        self.id = id
        self.title = title
        self.description = description
        self.channel = channel


def insert_items(raw_response, prev_result=[]):
    result = []
    response = raw_response.json()
    for video in response['items']:
        result.append(Video(video['id'], video['snippet']['title'],
                            video['snippet']['description'], video['snippet']['channelTitle']))
    next_page_token = None
    try:
        next_page_token = response['nextPageToken']
    except:
        print('There is no more next page token')

    return prev_result + result, next_page_token


def main():
    """
    GETTING YOUTUBE's TRENDING VIDEOS
    """
    initial_params = set_params()
    raw_response = get_raw_res(initial_params)

    if is_invalid_res(raw_response):
        return
    result, next_page_token = insert_items(raw_response)

    while next_page_token:
        req_params = set_params(next_page_token)
        raw_response = get_raw_res(req_params)
        if is_invalid_res(raw_response):
            return
        result, next_page_token = insert_items(raw_response, result)
    print(f"""
*********RESULT*********
ALL VIDEOS : {len(result)}
          
VIDEO DATA TITLE & CHANNEL
          """)
    titles = [x.__dict__['title'] for x in result]
    channels = [x.__dict__['channel'] for x in result]
    for idx in range(len(titles)):
        print(f"TITLE : {titles[idx]}")
        print(f"CHANNEL : {channels[idx]}")


if __name__ == '__main__':
    main()
