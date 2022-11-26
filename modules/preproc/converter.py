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
                    albuns_dict[album][1].append(track.get('song').get("lyrics")) 
                else:
                    albuns_dict[album] = (album,[track.get('song').get("lyrics")])

        self.albuns_dict = albuns_dict

    def make_csv(self):

        albuns = self.albuns_dict

        df_album_dict = {'album':[],
                         'lyric':[],}

        for album_id in albuns:
            for lyric in albuns[album_id]:
                df_album_dict['album'].append(album_id)
                df_album_dict['lyric'].append(lyric)
        
        df_albuns = pd.DataFrame.from_dict(df_album_dict)

        df_albuns.to_csv('./data/csv/Lyrics.csv')
        