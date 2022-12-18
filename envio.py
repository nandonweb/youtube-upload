import datetime
import time
from googleapiclient.http import MediaFileUpload
import pandas as pd
from google_apis import create_service
from termcolor import colored

# Printa as Categorias

def video_categories():
    video_categories = service.videoCategories().list(part='snippet', regionCode='US').execute()
    df = pd.DataFrame(video_categories.get('items'))
    return pd.concat([df['id'], df['snippet'].apply(pd.Series)[['title']]], axis=1)

# OAuth2
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube']
# SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
client_file = 'client-secret.json'
service = create_service(client_file, API_NAME, API_VERSION, SCOPES)

#print(video_categories())

"""
Passo 1. Envia o Video
"""
upload_time = (datetime.datetime.now() + datetime.timedelta(days=10)).isoformat() + '.000Z'
request_body = {
    'snippet': {
        'title': 'Teste 2',
        'description': 'Youtube bot video',
        'categoryId': '28',
        'tags': ['teste video, fdm, teste bot']
    },
    'status': {
        'privacyStatus': 'private',
        'publishedAt': upload_time,
        'selfDeclaredMadeForKids': False
    },
    'notifySubscribers': False
}

video_file = 'C:/Users/win11/Videos/fdm.mp4'
media_file = MediaFileUpload(video_file)

response_video_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=media_file
).execute()
uploaded_video_id = response_video_upload.get('id')


"""
Passo 2. Enviar a Thumbnail
"""
# response_thumbnail_upload = service.thumbnails().set(
#     videoId=uploaded_video_id,
#     media_body=MediaFileUpload('thumbnail.png')
# ).execute()

print(colored('Video Enviado com Sucesso!', 'green'))
