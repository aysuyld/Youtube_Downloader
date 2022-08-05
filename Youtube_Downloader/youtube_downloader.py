from pytube import YouTube

print("\nYouTube video indirme programına hoşgeldiniz..")

link = []
link = input("İndirmek istediğiniz youtube video linkini buraya yazınız: ")

url = YouTube(str(link))
video = url.streams.first()
video.download()