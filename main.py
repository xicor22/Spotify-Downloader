import os
print('''𝙨𝙥𝙤𝙩𝙞𝙛𝙮 𝙙𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙚𝙧
            by xicor22''')
file=open("location.txt", "r")
f1=file.read()
def single():
    link=str(input("Enter the link: "))
    command="spotdl -s "+link+" --output-file "+f1
    os.system(command)
def playlist():
    link=str(input("Enter the link: "))
    command="spotdl --playlist "+link+" --write-to= "+f1+" playlist_song_link.txt"
    os.system(command)
    command1="spotdl --list "+f1+" playlist_song_link.txt --output-file "+f1
    os.system(command1)
def main():
    option=int(input('''Choose from the following options:
(1) Single song
(2) Playlist
(3) All liked songs
(99) Exit
Enter here: '''))
    if option==1:
        single()
    elif option==2:
        playlist()
    elif option==3:
        print('''1. Install the desktop client of spotify.
2. Login with your credentials, create a new Playlist and goto liked songs.
3. Press 'ctrl + a' until all songs are selected as each press only selects 100 songs.
4. Right click and add all the selected songs to the newly created playlist.
5. Copy the playlist link and enter below.''')
        playlist()
    elif option==99:
        exit()
    else:
        print("Enter a valid option: ")
        main()
main()
