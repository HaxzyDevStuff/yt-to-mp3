import youtube_dl
import os


class YtToMp3:

    global txt 
    txt= """
██╗   ██╗████████╗████████╗ ██████╗ ███╗   ███╗██████╗ ██████╗ 
╚██╗ ██╔╝╚══██╔══╝╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗╚════██╗
 ╚████╔╝    ██║      ██║   ██║   ██║██╔████╔██║██████╔╝ █████╔╝
  ╚██╔╝     ██║      ██║   ██║   ██║██║╚██╔╝██║██╔═══╝  ╚═══██╗
   ██║      ██║      ██║   ╚██████╔╝██║ ╚═╝ ██║██║     ██████╔╝
   ╚═╝      ╚═╝      ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═════╝                              
"""
    def menu():
        print(txt)
        input("\n\n\nPress any key to enter the downloads: ")
        YtToMp3.proccess()
        

    def proccess():
        os.system('cls')
        print(txt)
        video = input("\n\n\nInsert video url: ")
        video_info = youtube_dl.YoutubeDL().extract_info(url = video, download=False)

        file = "{}.mp3".format(video_info['title'])
        options={
        'format':'bestaudio/best',
        'keepvideo': False,
        'outtmpl': file,
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        
        print("\n\nDownload complete... {}".format(file))
