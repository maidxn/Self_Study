import scrapy
from pymkv import MKVFile, MKVTrack
import os


SUBS_DIR = "D:\Study\Japanese\Boku no Hero Academia S1 (01-13) (Webrip)"
MKV_DIR = "D:\Study\Japanese\S01"
sub = os.listdir(SUBS_DIR)[0]
video = os.listdir(MKV_DIR)[0]
video = os.path.join(MKV_DIR, video)
sub = os.path.join(SUBS_DIR, sub)

mkv = MKVFile()
mkv.add_track(MKVTrack(video, track_id=0))
mkv.add_track(MKVTrack(video, track_id=2))
track_sub = MKVTrack(sub, language='jpn', forced_track=True)
mkv.add_track(track_sub)

mkv.mux("D:\Study\Japanese\Merged\S1E1_Merged.mkv")

# class NewsSpider(scrapy.Spider):
#     name = "anime" 

#     def start_requests(self):
#        urls = [
#             'https://animelool.com/Anime/ENDED/B/Boku%20no%20Hero%20Academia/S01/1080p/'
#         ]