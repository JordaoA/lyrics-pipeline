import os
import json
import lyricsgenius


class Extract_lyrics():
    
    def __init__(self):
        
        config = open('config.json', 'r+')
        config_json = json.load(config)

        # Client access token
        token = config_json.get('client_access_token')

        self.albuns = config_json.get('albuns')

        self.artist = config_json.get('artist')

        self.genius = lyricsgenius.Genius(token)


    def save_lyrics(self):
        format_albuns = []

        # format names
        for album in self.albuns:
            formated_title = ''
            
            for atom in album:
                if atom.isalpha() or atom.isdigit():
                    formated_title += atom
            
            format_albuns.append(formated_title)

        # extract and save lyrics
        for album in self.albuns:
            album_ = self.genius.search_album(album, self.artist)
            album_.save_lyrics()

        # saving formated titles
        formated_albuns = {'format_albuns': format_albuns}

        formated_ = open('albuns.json', 'w')
        json.dump(formated_albuns, formated_)

        # moving json files
        os.system("mv Lyrics_* ./data/json/")