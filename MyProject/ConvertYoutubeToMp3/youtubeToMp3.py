from pytube import YouTube
import time


def GetMp3File(arr_url, arr_name, pos):
    yt = YouTube(arr_url[pos])
    file = yt.streams.get_audio_only()
    name = arr_name[pos] + '.mp3'
    file.download(output_path=r'D:/Code/python/pythonProject/Music', filename=name)
    print("Done!", name, arr_url[pos], pos)


url_file = open(r'D:/Code/python/pythonProject/url.txt', "r")
url_arr = url_file.read()
urls = url_arr.splitlines()
url_file.close()

name_file = open(r'D:/Code/python/pythonProject/name.txt', "r")
name_arr = name_file.read()
names = name_arr.splitlines()
name_file.close()

for item in range(len(urls)):
    GetMp3File(urls, names, item)
    time.sleep(5)

# url = 'https://www.youtube.com/watch?v=uQo8mUEqkkE&list=PLDn9IICB2Wiv2JFCUgP9SPLikmeBax00U'
# yt = YouTube(url)
# print(yt.streams.filter(only_audio=True))
# a = yt.streams.get_audio_only()
# a.download()

