# =====================================================================================================
# 編寫平台: Windows 10 
# 編寫人: chickenlegyummy 
# 編寫日: 2024-02-15 3:58 AM GMT+8
# Latest edit: 2024-11-21 2:11 AM GMT+8 - fixed HTTP Error 403: Forbidden
# 後記: 老子發現google到既youtube mp3 啲網太sus 所以寫左呢一個program
# 注意: 每段片 or 音源都係最高品質 
#           get_highest_resolution() ---- 識英文就解到 
#           get_audio_only ---- pytube default 就係最屌音質
# =====================================================================================================

import re
from pytube import Playlist
import subprocess
import os
from pytube.innertube import _default_clients

_default_clients["ANDROID"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["ANDROID_EMBED"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_EMBED"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_MUSIC"]["context"]["client"]["clientVersion"] = "6.41"
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID"]

def get_ffmpeg_path():
    while True:
        path = input("請輸入FFmpeg執行檔的路徑 (ffmpeg\\bin\\ffmpeg.exe) : \n").strip()
        if os.path.isfile(path):
            return path
        else:
            print("提供的路徑無效。請再試一次。")

def check_ffmpeg_path(path):
    try:
        subprocess.run([path, "-version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def run_ffmpeg(ffmpeg_path, input_file, output_file):
    try:
        process = subprocess.Popen([
            ffmpeg_path,
            '-i', input_file,
            output_file
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='replace')
        
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            print(f"FFmpeg執行失敗。錯誤碼: {process.returncode}")
            print(f"錯誤訊息: {stderr}")
            return False
        return True
    except FileNotFoundError:
        print(f"找不到FFmpeg執行檔: {ffmpeg_path}")
        return False
    except Exception as e:
        print(f"執行FFmpeg時發生錯誤: {str(e)}")
        return False

def entry(option):
    global ffmpeg_path
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

            print("\n您下載緊既係... " + title)
            print("\n轉檔中...")
            ## pytube既預設音檔係mp4, 而os.rename做mp3 =/= 轉檔做mp3, 利用ffmpeg轉檔
            input_file = os.path.join(default_download_directory, title + '.mp4')
            output_file = os.path.join(default_download_directory, new_title)

            while True:
                if run_ffmpeg(ffmpeg_path, input_file, output_file):
                    break
                else:
                    print(f"無法使用當前的FFmpeg路徑: {ffmpeg_path}")
                    retry = input("是否要嘗試輸入新的FFmpeg路徑? (y/n): ").lower()
                    if retry != 'y' or retry !="Y":
                        print("操作已取消。")
                        return
                    ffmpeg_path = get_ffmpeg_path()

            os.remove(input_file)  # 刪除原檔
            print("\n轉檔完成")
            print("\n"+title+"下載完成 已完成下載數目: "+ str(count))

        print("搞掂!! O.Ob")
        again()

    else:
 
        print("輸入錯誤...")
        entry(input("影片(v) or 音樂(m)?: "))

def again():

    go = input("\n仲有冇野要down (Y/N): ")
    if go == "Y" or go == "y":
        entry(input("\n影片(v) or 音樂(m)?: "))
    else:
        print("收到你 放工返屋企食飯~ ></")

default_ffmpeg_path = './ffmpeg/bin/ffmpeg'
if check_ffmpeg_path(default_ffmpeg_path):
    ffmpeg_path = default_ffmpeg_path
    print(f"已找到FFmpeg: {ffmpeg_path}")
else:
    print("未找到預設的FFmpeg路徑。")
    ffmpeg_path = get_ffmpeg_path()

print("\n===================================================")
print("成功載入 Python Youtube MP4 / MP3 下載器")
print("以後唔洗再驚上網down野比人hack")

default_download_directory = input("\n輸入下載路徑:\n")

entry(input("\n影片(v) or 音樂(m)?: "))