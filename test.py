from __future__ import unicode_literals
from ytmusicapi import YTMusic
import azapi
import youtube_dl
import wget

## Search songs
# Uses data from YouTube Music. 
song_name = input('Enter song name: ')
ytmusic = YTMusic('headers_auth.json') # "headers_auth.json" contains a YouTube Music cookie. Refer to ytmusicapi documentation.
search_results = ytmusic.search(song_name, 'songs') # Filters the search results to only show "songs".

## List Songs
# This is fucking unreadable.
counter = 1 
for i in search_results: 
    print(counter, '\033[95m\033[1m', i['title'], '\033[0m', 'by', '\033[1m\033[96m', i['artists'][0]['name'], '\033[0m', 'from', '\033[1m\033[91m', i['album']['name'], '\033[0m')
    counter += 1

## Select a song from the list
selectedSong = search_results[int(input('Select a song to download.')) - 1]

## Song Downloader
# Uses youtube-dl.
ydl_opts = {
     'format' : 'bestaudio',
     'outtmpl' : selectedSong['artists'][0]['name'] + ' - ' + selectedSong['title'] + '.m4a',
     'quiet' : 'true'
     }
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     ydl.download([selectedSong['videoId']])
print('✅ Downloaded \033[95m\033[1m', selectedSong['title'], '\033[0m')

## Thumbnail Grabber
# Grabs album art from Youtube Music with ytmusicapi. 
thumbnailURL = selectedSong['thumbnails'][0]['url'].split('=')[0] # Since the thumbnail URL contains image dimensions, this splits size data off to save in highest resolution available.
wget.download(thumbnailURL, 'thumbnail.jpg') # There's probably a better solution than wget but ¯\_(ツ)_/¯

# Lyrics Collector
# Data is acquired from AZLyrics.com using azapi.

api = azapi.AZlyrics() 

api.artist = selectedSong['artists'][0]['name']
api.title = selectedSong['title']

api.getLyrics(save=True) # Saves the lyrics as a (Title) - (Artist).txt
