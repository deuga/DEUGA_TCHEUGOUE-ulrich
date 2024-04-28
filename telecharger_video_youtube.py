import cv2
import pafy
import os
os.environ["PAFY_BACKEND"] = "internal"
from pytube import YouTube

video_url = "https://youtu.be/_nTmFQbqsJY?si=6zvmBQ2v_lLj2L2x"
yt = YouTube(video_url)
stream = yt.streams.get_highest_resolution()
stream.download(output_path=".", filename="video.mp4")
