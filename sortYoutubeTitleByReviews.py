#!/usr/bin/python

def score(line):
    return long(line.split("\t")[2])

if __name__ == "__main__":
    orderedList = []
    kind = "video"
    if kind == "playlist":
        file = open("top100videoTitle_ID_Reviews.txt")
    else:
        file = open("top100videoTitle_ID_Reviews.txt")

    for i,line in enumerate(sorted(file, key=score, reverse=True)):
        print(line)
        orderedList.append(str(i) + " " + line)

    outfile = open("top100" + kind + "SortedListByReviews.txt", 'w')
    outfile.write("".join(orderedList))