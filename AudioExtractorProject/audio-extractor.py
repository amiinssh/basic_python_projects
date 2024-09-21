import moviepy.editor as mp
import os

path = input("Enter the videos path: ")

videoclip = mp.VideoFileClip(path)
audioclip = videoclip.audio
audioclip.write_audiofile("audio.mp3")

