from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo
import urllib.request

# loggin into the channel
channel = Channel()
channel.login("client_secret_692791888419-25kcgjfivl3mal9lgknbsspd15p6flfv.apps.googleusercontent.com.json", "credentials.storage")

urllib.request.urlretrieve("https://www.utdallas.edu/files/2022/10/B-1.mp4", "video.mp4")
# setting up the video that is going to be uploaded
video = LocalVideo(file_path="video.mp4")

# setting snippet
video.set_title("UTD Title")
video.set_description("This is a description")
video.set_tags(["this", "tag"])
video.set_category("gaming")
video.set_default_language("en-US")

# setting status
video.set_embeddable(True)
video.set_license("creativeCommon")
video.set_privacy_status("private")
video.set_public_stats_viewable(True)

# setting thumbnail
# video.set_thumbnail_path('test_thumb.png')
video = channel.upload_video(video)
print(video.id)
print(video)