from __future__ import unicode_literals
from ytmusicapi import YTMusic
import youtube_dl
import logging
song_name = input('Enter song name ')
ytmusic = YTMusic('headers_auth.json')
search_results = ytmusic.search(song_name, 'songs')


# List Songs

for i in range(10): 
    print(i+1, '\033[95m\033[1m', search_results[i]['title'], '\033[0m', 'by', '\033[1m\033[96m', search_results[i]['artists'][0]['name'], '\033[0m', 'from', '\033[1m\033[91m', search_results[i]['album']['name'], '\033[0m')


# Select a song from the list
selectedSong = search_results[int(input('Select a song to download.')) - 1]

# Downloader
ydl_opts = {
     'format' : 'bestaudio',
     'outtmpl' : selectedSong['artists'][0]['name'] + ' - ' + selectedSong['title'] + '.m4a',
     'quiet' : 'true'
     }
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     ydl.download([selectedSong['videoId']])
print('✅ Downloaded \033[95m\033[1m', selectedSong['title'], '\033[0m.')

