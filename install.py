import os
path=str(input("Enter the location of the directory where you want to download the songs: "))
file=open("location.txt","x")
file.write(path)
file.close()
f1=open("spotify","x")
f1.write("python /data/data/com.termux/files/home/SpotifyDownloader/main.py")
os.system("mv music /data/data/com.termux/files/usr/bin")
os.system("chmod +x /data/data/com.termux/files/usr/bin/spotify")
