#!/usr/bin/python

def score(line):
    return long(line.split("\t")[1])

if __name__ == "__main__":
    orderedList = []
    kind = "video"
    if kind == "playlist":
        file = open("topTracksFromYouTube.txt")
    else:
        file = open("topTracksFromYouTube.txt")

    for i,line in enumerate(sorted(file, key=score, reverse=True)):
        print(line)
        orderedList.append(str(i) + " " + line)

    outfile = open("top100YouTube" + kind + "SortedListByReviews.txt", 'w')
    outfile.write("".join(orderedList))