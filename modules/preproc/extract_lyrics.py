import os
import json
import lyricsgenius

config = open('../../config.json', 'r+')
config_json = json.load(config)

#Client access token
token = config_json.get('client_access_token')

genius = lyricsgenius.Genius(token)

albuns = config_json.get('albuns')

artist = config_json.get('artist')

format_albuns = []


# format names
for album in albuns:
    formated_title = ''
    
    for atom in album:
        if atom.isalpha() or atom.isdigit():
            formated_title += atom
    
    format_albuns.append(formated_title)


# extract and save lyrics
for album in albuns:
    album_ = genius.search_album(album, artist)
    album_.save_lyrics()


# saving formated titles
formated_albuns = {'format_albuns': format_albuns}

formated_ = open('albuns.json', 'w')
json.dump(formated_albuns, formated_)

# moving json files
os.system("mv Lyrics_* ../../data/json/")