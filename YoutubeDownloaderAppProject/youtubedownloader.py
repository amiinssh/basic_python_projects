import youtube_dl


url = input("Please provide the link to your video: ")

with youtube_dl.YoutubeDL() as ydl:
    ydl.download([url])