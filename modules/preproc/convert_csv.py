import json
import pandas as pd

albuns = open('./albuns.json', 'r+')

albuns_json = json.load(albuns)

albuns_json.get("format_albuns")
