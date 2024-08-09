# =====================================================================================================
# 編寫平台: Windows 10 
# 編寫人: chickenlegyummy 
# 編寫日: 2024-05-18 3:58 AM GMT+8
# 後記: 老子發現google到既youtube mp3 啲網太sus 所以寫左呢一個program
# 注意: 每段片 or 音源都係最高品質 
#           get_highest_resolution() ---- 識英文就解到 
#           get_audio_only ---- pytube default 就係最屌音質
# =====================================================================================================

import re
from pytube import Playlist
import subprocess
import os

ffmpeg_path = './ffmpeg/bin/ffmpeg'

print("\n===================================================")
print("成功載入 Python Youtube Playlist MP4 / MP3 下載器")
print("以後唔洗再驚上網down野比人hack")

default_download_directory = input("\n輸入下載路徑:\n")

def entry(option):
    if option == "v" or option == "V":
        
        url = input("\n輸入連結\n")
        videos = Playlist(url)
        count = 0
        print("\n您下載緊既播放清單係... " + videos.title + "\n影片數目: " + str(len(videos)))
        for video in videos.videos:
            count += 1
            file = video.streams.get_highest_resolution().download(default_download_directory)
            title = re.sub(r'[\\/:"*?<>|,\'`~.#]', '', video.title)
            ## os.rename(file, title + '.mp4')
            os.rename(file, os.path.join(default_download_directory, title + '.mp4')) ## 如果你想download directory唔係launcher度
            print("\n"+title+"下載完成 已完成下載數目: "+ str(count))
        print("搞掂!! O.Ob")
        again()

    elif option == "m" or option == "M":

        url = input("\n輸入連結\n")
        videos = Playlist(url)
        count = 0
        print("\n您下載緊既播放清單係... " + videos.title + "\n影片數目: " + str(len(videos)))
        for video in videos.videos:
            count += 1
            file = video.streams.get_audio_only().download(default_download_directory)
            title = re.sub(r'[\\/:"*?<>|,\'`~.#]', '', video.title)

            os.rename(file, os.path.join(default_download_directory, title + '.mp4')) ## 如果你想download directory唔係launcher度
            ## os.rename(file, title + '.mp4')
            new_title = title + ".mp3"
            print("\n轉檔中...")
            ## pytube既預設音檔係mp4, 而os.rename做mp3 =/= 轉檔做mp3, 利用ffmpeg轉檔
            subprocess.run([
                ffmpeg_path,
                '-i', os.path.join(default_download_directory, title + '.mp4'),
                os.path.join(default_download_directory, new_title)
            ])       
            os.remove(file) ## del原檔
            print("\n轉檔完成")
            print("\n"+title+"下載完成 已完成下載數目: "+ str(count))
        print("搞掂!! O.Ob")
        again()

    else:
 
        print("輸入錯誤..字都唔撚識睇?")
        entry(input("影片(v) or 音樂(m)?: "))

def again():

    go = input("\n仲有冇野要down (Y/N): ")
    if go == "Y" or go == "y":
        entry(input("\n影片(v) or 音樂(m)?: "))
    else:
        print("收到你 放工返屋企食飯~ ></")


entry(input("\n影片(v) or 音樂(m)?: "))
