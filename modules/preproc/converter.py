import json
import pandas as pd

class Csv_converter():
    
    def __init__(self):
        
        albuns = open('./albuns.json', 'r+')

        albuns_json = json.load(albuns)

        self.albuns = albuns_json.get("format_albuns")

    def converter(self):

        albuns = self.albuns

        albuns_dict = {}

        for album in albuns:
            #Lyrics_HolocaustoUrbano
            album_name = f'Lyrics_{album}.json'

            album_ = open(f"./data/json/{album_name}", 'r+')

            albuns_json = json.load(album_)

            tracks = albuns_json.get("tracks")                        
            
            for track in tracks:
                
                if albuns_dict.get(album):
                    albuns_dict[album].append(track.get('song').get("lyrics")) 
                else:
                    albuns_dict[album] = [track.get('song').get("lyrics")]

        return albuns_dict