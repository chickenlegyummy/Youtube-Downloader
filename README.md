# Rifu YT影片下載器
一個無病毒 無廣告 開源的簡單Youtube下載器

## 原理
### pytube
利用 pytube library 把youtube的影片捉下來，再輸出成mp4影片/mp3音檔

### FFmpeg
透過 FFmpeg 把捉下來的mp4音檔轉換成mp3音檔，主要用在下載mp3音檔

## 使用方法 (推薦使用方法2)
方法1:
1. 直接下載最新release的壓縮檔
2. 解壓縮就可以直接使用

方法2:
1. 直接下載最新release的壓縮檔
2. 自行下載pytube library 連結: https://github.com/pytube/pytube
3. 解壓縮並找出原始碼的python script
4. 利用ide/cmd等各種方法開啟python script
5. 開啟成功可以直接使用
   
### 如使用方法1
打包的exe檔裏的pytube是本人當下使用的版本，而youtube經常更改一些程式，所以很有可能你正在使用的版本已經失效了。
如我還未進行downloader的版本更新，並且你在使用時已經失效，可以參考下面方法2的注意事項。
### 如使用方法2
因為方法2不會使用我提供的exe檔，而是直接開啟script來運行，可以自己在pytube的repo中查看社群維護的bug fix。
通常會發生bug的原因是pytube中cipher.py第27X行左右未趕上youtube的更新，pytube repo會有人po出solution，可以自己copy修改cipher.py

## 注意
我是一個普通的程式初學者，寫得可能不太好，勿屌小弟，小弟玻璃心會碎的，但是有意見給我可以改進的話完全沒有問題!! ><

# References
FFmpeg https://www.ffmpeg.org <br />
pytube https://github.com/pytube/pytube
