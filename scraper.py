import pytube
from googleapiclient.discovery import build
import random

DEVELOPER_KEY = 'YOUTUBE_API_KEY'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

prefix = ['IMG ', 'IMG_', 'IMG-', 'DSC ']
postfix = [' MOV', '.MOV', ' .MOV']

def youtube_search():
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=random.choice(prefix) + str(random.randint(999, 9999)) + random.choice(postfix),
    part='snippet',
    maxResults=5
  ).execute()

  videos = []

  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s' % (search_result['id']['videoId']))
  return (videos[random.randint(0, 2)])

while True:

    a = 'https://ww.youtube.com/watch?v=' + youtube_search()


    video_url = a
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.first()
    video.download('./videos')
