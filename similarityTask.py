def addVector(trackVectorsCollection, chart, type):
    for i,line in enumerate(chart):
        title = line.split("\t")[0].strip();
        if not trackVectorsCollection.has_key(title):
            trackVectorsCollection[title] = {type : i}
        else:
            trackVectorsCollection[title][type] = i



amazonFileName = "top100trackAmazonTitle.txt"
youtubeFileName = "top100videoSortedListByReviewsBefore2017.txt"
amazonRank = open(amazonFileName)
youtubeRank = open(youtubeFileName)

trackVectorsCollection = {}
addVector(trackVectorsCollection,amazonRank,"amazon")
addVector(trackVectorsCollection,youtubeRank,"youtube")


youtubePlaceList = []
amazonPlaceList = []
listToFile = []
for item in trackVectorsCollection.values():
    if item.has_key("amazon") and item.has_key("youtube"):
        youtubePlaceList.append(item["amazon"])
        amazonPlaceList.append(item["youtube"])
        listToFile.append(str(item["amazon"]) + " " + str(item["youtube"]))

outfile = open("TracksTwoSourceVectorsBefore2017.txt", 'wb')
outfile.write("\n".join(listToFile))
print trackVectorsCollection

