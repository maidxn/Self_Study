from pytube import YouTube
import time


#Maybe you've already known, the Youtube new version from 2022 is no longer to be get streams
#By pytube :<<<


def GetMp3File(arr_url, arr_name, pos):
    yt = YouTube(arr_url[pos])
    file = yt.streams.get_audio_only()
    name = arr_name[pos] + '.mp3'
    file.download(output_path=r'D:/Code/python/pythonProject/Music', filename=name)
    print("Done!", name, arr_url[pos], pos)


url_file = open(r'D:/Code/python/pythonProject/MyProject/ConvertYoutubeToMp3/url.txt', "r")
url_arr = url_file.read()
urls = url_arr.splitlines()
url_file.close()

name_file = open(r'D:/Code/python/pythonProject/MyProject/ConvertYoutubeToMp3/name.txt', "r")
name_arr = name_file.read()
names = name_arr.splitlines()
name_file.close()

for item in range(len(urls)):
    GetMp3File(urls, names, item)
    time.sleep(5)

# url = 'https://www.youtube.com/watch?v=3Uo0JAUWijM'
# yt = YouTube(url)
# print(yt.streams)
# name = "HappyNewYear.mp3"
# file = yt.streams.get_audio_only()
# file.download(output_path=r'D:/Code/python/pythonProject/Music', filename=name)
# print(file)