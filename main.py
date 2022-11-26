from modules.preproc.converter import Csv_converter
from modules.preproc.extract_lyrics import Extract_lyrics

extractor = Extract_lyrics()
extractor.save_lyrics()

converter = Csv_converter()
all_lyrics = converter.converter()