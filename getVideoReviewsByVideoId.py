#!/usr/bin/python

import os

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

def youtube_video(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  video_response = youtube.videos().list(
    id=options.id,
    part="id,statistics"
  ).execute()

  videos = []
  channels = []
  playlists = []


  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for video_result in video_response.get("items", []):
    if video_result["kind"] == "youtube#video":
      return video_result["id"], video_result["statistics"]["viewCount"]
    elif video_result["kind"] == "youtube#channel":
      return video_result["id"], video_result["statistics"]["viewCount"]
    elif video_result["kind"] == "youtube#playlist":
      return video_result["id"], video_result["statistics"]["viewCount"]

if __name__ == "__main__":
  kind = "video"
  listOfReviews = []
  if kind == "playlist":
    file = open("top100playlistId.txt")
  else:
    file = open("top100videoId.txt")

  argparser.add_argument("--id", help="video_id", default="")
  args = argparser.parse_args()
  for video_id in file:
    videoID = video_id.split("\t")[1]
    try:
      args.id = videoID
      videoId, videoReview = youtube_video(args)
      if videoId and videoReview:
        listOfReviews.append(video_id.split("\t")[0] + "\t" + videoId.encode('utf-8') + "\t" + videoReview.encode('utf-8'))
        print listOfReviews[-1].split("\t")
    except HttpError, e:
      print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

  print [line.split("\t") for line in listOfReviews]

  outfile = open("top100" + kind + "Title_ID_Reviews.txt", 'w')
  outfile.write("\n".join(listOfReviews))