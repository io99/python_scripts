from bs4 import BeautifulSoup
import requests
 
band = input("What band sings the song you want the lyrics for? ")
song = input("Which {0} song would you like the lyrics for? ".format(band))
 
band = band.replace(" ","-")
band = band + "-"
 
song = song.lower()
song = song.replace(" ","-")
song = song + "-lyrics"
 
link = "https://genius.com/{0}{1}".format(band,song)
print("Source:",link)
 
page = requests.get(link)
html = BeautifulSoup(page.text, "html.parser")
 
try:
    lyrics = html.find("div", class_="lyrics").get_text()
    print(lyrics)
except AttributeError:
    print("Song not found, sorry!")