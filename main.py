import os
import json

from googleapiclient.discovery import build


class Channel:

    def __init__(self, channel_id):
        self.channel_id = channel_id
        api_key: str = os.getenv('API_UT')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def print_info(self):
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
vdud.print_info()

