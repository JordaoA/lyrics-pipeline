from modules.preproc.converter import Csv_converter
from modules.preproc.extract_lyrics import Extract_lyrics

class LyricsPipeline():

    def run(self):
        extractor = Extract_lyrics()
        extractor.save_lyrics()
        
        converter = Csv_converter()
        converter.converter()
        converter.make_csv()

if __name__ == "__main__":
    lyric = LyricsPipeline()
    lyric.run()