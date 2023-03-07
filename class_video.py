import os
from class_mixin_service import MixinService


class Video(MixinService):
    def __init__(self, video_id):
        self.video_id = video_id
        youtube = self.get_service()
        self.video_response = youtube.videos().list(part='snippet,statistics', id=video_id).execute()
        self.title = self.video_response['items'][0]['snippet']['title']
        self.view_count = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count = self.video_response['items'][0]['statistics']['likeCount']


    def __str__(self):
        return self.title


