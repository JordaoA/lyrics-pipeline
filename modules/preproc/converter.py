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
            album_name = f'Lyrics_{album}.json'

            album_ = open(f"./data/json/{album_name}", 'r+')

            albuns_json = json.load(album_)

            tracks = albuns_json.get("tracks")                        
            
            for track in tracks:
                
                title = track.get('song').get("path")

                artist = title[1:14]
                title = title[15:len(title)-7]
                lyric = track.get('song').get("lyrics")

                if albuns_dict.get(album):
                    albuns_dict[album].append((artist,title,lyric)) 
                else:
                    albuns_dict[album] = [(artist,title,lyric)]

        self.albuns_dict = albuns_dict

    def make_csv(self):

        albuns = self.albuns_dict

        df_album_dict = {'album':[],
                         'lyric':[],
                         'title':[],
                         'artist':[]}

        for album_id in albuns:
            for song in albuns[album_id]:
                df_album_dict['album'].append(album_id)
                df_album_dict['lyric'].append(song[2])
                df_album_dict['title'].append(song[1])
                df_album_dict['artist'].append(song[0])
        
        df_albuns = pd.DataFrame.from_dict(df_album_dict)

        df_albuns.to_csv('./data/csv/Lyrics.csv')
        