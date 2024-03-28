from pytube import Playlist, YouTube
import pandas as pd

link = input("Enter Your Playlist URL")

playlist = Playlist(link)



print("Playlist Name = ", playlist.title)
print("Total No of Videos" , playlist.length)


dict = {"Title":[], "Link": []}

df = pd.DataFrame(dict)

vtitles= []

for i in playlist:
    vtitles.append(YouTube(i).title)

df["Title"] = vtitles
df["Link"] = playlist

df.to_excel("Playlist.xlsx")

print("Playist Extracted completed")