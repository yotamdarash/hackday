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


def youtube_search(options, kind="video"):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results
    ).execute()
    for search_result in search_response.get("items", []):
        if kind == "video":
            if search_result["id"]["kind"] == "youtube#video":
                return search_result["snippet"]["publishedAt"], search_result["id"]["videoId"]
        elif kind == "playlist":
            if search_result["id"]["kind"] == "youtube#playlist":
                return search_result["snippet"]["publishedAt"], search_result["id"]["playlistId"]


if __name__ == "__main__":
    kind = "video"
    listOfIds = []
    if kind == "playlist":
        file = open("top500albumAmazonTitle.txt")
    else:
        file = open("top1000trackAmazonInDETitle.txt")
    argparser.add_argument("--q", help="Search term", default="none")
    argparser.add_argument("--max-results", help="Max results", default=1)
    args = argparser.parse_args()
    for line in file:
        line = re.sub("[\(\[].*?[\)\]]", "", line)
        line = line.rstrip()
        args.q = line
        try:
            resultID, resultTimeInYoutube = youtube_search(args, kind);
            if resultID and resultTimeInYoutube:
                listOfIds.append(line + "\t" + resultTimeInYoutube.encode('utf-8') + "\t" + resultID.encode('utf-8'))
                print listOfIds[-1].split("\t")
        except:
            print "Error getting data"

    print [line.split("\t") for line in listOfIds]

    outfile = open("top100" + kind + "IdDE.txt", 'w')
    outfile.write("\n".join(listOfIds))


