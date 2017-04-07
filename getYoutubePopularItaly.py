#!/usr/bin/python
import re

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
# DEVELOPER_KEY = "649396978149-4ovm5vrkakjn1hgas7sfd41rb72il29m.apps.googleusercontent.com"
DEVELOPER_KEY = "AIzaSyBE4XG36W8hToue7UbHt224atQ69iGcuCw"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.videos().list(
        videoCategoryId=10,
        part="snippet,statistics",
        chart="mostPopular",
        maxResults=50,
        pageToken=options.pageToken,
        regionCode = "IT"
    ).execute()
    trackList = []
    for search_result in search_response.get("items", []):
        if search_result["kind"]== "youtube#video":
            try:
                trackList.append([search_result["snippet"]["title"].encode('utf-8'), search_result["statistics"]["viewCount"].encode('utf-8')])
            except:
                print "could not get a field"
    return trackList, search_response.get("nextPageToken", [])

if __name__ == "__main__":
    listOfTracks = []
    argparser.add_argument("--pageToken", help="Search term", default="")
    args = argparser.parse_args()
    while len(listOfTracks)< 200 :
        listOfTracksFromPage, nextPage = youtube_search(args)
        listOfTracks = listOfTracks + listOfTracksFromPage
        args.pageToken = nextPage


    for i,line in enumerate(listOfTracks):
        name = line[0];
        name = re.sub("[\(\[].*?[\)\]]", "", name)
        # name = ''.join(name.partition(' - ')[1:])
        name = ''.join(name.partition(' - ')[1:])
        name = name.lstrip("- 0123456789")
        listOfTracks[i][0] = name
        # listOfTracksFromPage[0] = name
        #
    outfile = open("TopTracksFromYouTubeItaly.txt",'w')
    outfile.write("\n".join(["\t".join(line) for line in listOfTracks]))


    # kind = "video"
    # listOfIds = []
    # if kind == "playlist":
    #     file = open("top500albumAmazonTitle.txt")
    # else:
    #     file = open("top100trackAmazonTitle.txt")
    # argparser.add_argument("--q", help="Search term", default="none")
    # argparser.add_argument("--max-results", help="Max results", default=1)
    # args = argparser.parse_args()
    # for line in file:
    #     line = re.sub("[\(\[].*?[\)\]]", "", line)
    #     line = line.rstrip()
    #     args.q = line
    #     try:
    #         resultID, resultTimeInYoutube = youtube_search(args, kind);
    #         if resultID and resultTimeInYoutube:
    #             listOfIds.append(line + "\t" + resultTimeInYoutube.encode('utf-8') + "\t" + resultID.encode('utf-8'))
    #             print listOfIds[-1].split("\t")
    #     except:
    #         print "Error getting data"
    #
    # print [line.split("\t") for line in listOfIds]
    #
    # outfile = open("top100" + kind + "Id.txt", 'w')
    # outfile.write("\n".join(listOfIds))
