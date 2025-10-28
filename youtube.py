from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

# ADD FOLDER HERE
yd.download('./YTfolder')

# Open your terminal and run the Python script (youtube.py) along with the YouTube link in quotes.
# python3 youtube.py "Your-YouTube-Video-Link"
