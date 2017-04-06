import json
from pprint import pprint
import re

with open('top100TracksAmazon.json') as data_file:
    data = json.load(data_file)

trackTitleList = []
for track in data["trackList"]:
    l = re.sub("[\(\[].*?[\)\]]", "", track["title"].encode('utf-8'))
    trackTitleList.append(l)

print trackTitleList
outfile = open("top100trackAmazonTitle.txt", 'w')
outfile.write("\n".join(trackTitleList))

# pprint(data)