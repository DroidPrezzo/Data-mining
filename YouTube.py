#First import YouTube from the pytube module
from pytube import YouTube

#Specify your download folder in the quotes. it should look like this /Users/user001/Downloads
DOWNLOAD_FOLDER = ""
#Put the youtube link in the quotes below eg https://www.youtube.com/watch?v=KlsYCECWEWE
video_url = ""
#This line calls the youtube method on the link to your video
video_obj = YouTube(video_url)
#This line specifies the video resolution you want
stream = video_obj.streams.get_highest_resolution()
#This line downloads the video to your specified path/folder
stream.download(DOWNLOAD_FOLDER)