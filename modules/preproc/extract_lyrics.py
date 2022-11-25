import json
import shutil
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

# move files
for album in format_albuns:
    original = f'/home/jordaoa/Documentos/nlp_project/modules/preproc/Lyrics_{album}.json'
    target = f'/home/jordaoa/Documentos/nlp_project/data/json/Lyrics_{album}.json'
    shutil.move(original, target)


formated_albuns = {'format_albuns': format_albuns}

# saving formated titles
formated_ = open('albuns.json', 'w')
json.dump(formated_albuns, formated_)