from pytubefix import YouTube
import subprocess
import os
print("""
███████╗ █████╗ ██╗   ██╗███████╗██╗     ██╗███╗   ██╗██╗  ██╗
██╔════╝██╔══██╗██║   ██║██╔════╝██║     ██║████╗  ██║██║ ██╔╝
███████╗███████║██║   ██║█████╗  ██║     ██║██╔██╗ ██║█████╔╝ 
╚════██║██╔══██║╚██╗ ██╔╝██╔══╝  ██║     ██║██║╚██╗██║██╔═██╗ 
███████║██║  ██║ ╚████╔╝ ███████╗███████╗██║██║ ╚████║██║  ██╗
╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
------->>>>>>>| ▄︻デ══━一一 ᴍᴀᴅᴇ ɪɴ ᴛᴜʀᴋᴇʏ :D |<<<<<<<--------""")
while True:
    link = input("""
╔===========================╗
╠--->>>>YOUTUBE LİNKİ<<<<---╣
╚===========================╝
『GİR』>:""")
    try:
        video = YouTube(link)
        #Burda video adını buluyoruz ve YASAKLI karakterler var ise Değiştiriyoruz :)
        videoAd = video.title
        for x in '<>:"/\\|?*':
            videoAd = videoAd.replace(x,"_")
        #Burda Video SES ve Kendisini En iyi halini buluyoruz
        VideoBulma = video.streams.filter(only_video=True,file_extension="mp4").order_by("resolution").desc().first()
        AudioBulma = video.streams.filter(only_audio=True,file_extension="mp4").order_by("abr").desc().first()
        #VİDEO İNDİRME ALANI!
        if VideoBulma and AudioBulma:
            print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
   VİDEO YÜKLENİYOR🔄           
 --->>>『⏱....』<<<---          
          🌞              
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀""")
            VideoBulma.download(output_path = ".",filename = "{}+.mp4".format(videoAd))
            AudioBulma.download(output_path = ".",filename = "{}(Aduio)+.mp4".format(videoAd))
            #Burda VİDEO Birleştiriyoruz
            subprocess.run([ "ffmpeg","-y", "-i", "{}+.mp4".format(videoAd), "-i", "{}(Aduio)+.mp4".format(videoAd), "-c:v", "copy", "-c:a", "aac", "{}.mp4".format(videoAd) ])
            print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
   VİDEO YÜKLENDİ✅      
 ->>『GÜLE GÜLE🫶🏻』<<-       
          🌞
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄              
""")
            #Burda Birleştirmiş Videonun KONUMU VERİLİYOR
            konum = len(os.path.abspath("{}.mp4".format(videoAd)))
            print("""
{:▀^{}}
{:^{}}      
{:^8}

{:▀^{}}                """.format("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀",konum,"VİDEO KONUMU📌",konum,os.path.abspath("{}.mp4".format(videoAd)),"▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀",konum))
            #BURDA İSE SES VE NORMAL VİDEO SİLİYORUZ
            os.remove("{}(Aduio)+.mp4".format(videoAd))
            os.remove("{}+.mp4".format(videoAd))

    except:
        print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  VİDEO YÜKLENEMEDİ❌      
 ->>『Tekrar Dene』<<-       
          🤬              
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀""")
