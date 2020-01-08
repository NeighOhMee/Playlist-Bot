'''
Discord bot that adds the youtube videos in a channel to a playlist
Author: Yaw Amoa-Asare
'''
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import discord
from discord.ext import commands

#let youtube be a global variable
youtube = 0

def insertVideo(videoId):
	'''
	inserts videoId to the playlist with a youtube api call
	'''
	#TODO: keep duplicates from being added to the playlist
	global youtube
	request = youtube.playlistItems().insert(
        part="snippet",
        body={
          "snippet": {
            "playlistId": "PLEl38luv6tgnQvzjUKhLMUJr2jiB28gT4",
            "position": 0,
            "resourceId": {
              "kind": "youtube#video",
              "videoId": videoId
            }
          }
        }
    )
	response = request.execute()
	#print(response)

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
	'''
	On bot startup sets up the authorization for the youtube api
	'''
    global youtube
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    #os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    #TODO: make the verification automatic
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    print("Bot is ready")

@client.command(pass_contex=True)
async def test(ctx):
	'''
	debugging command
	'''
	#hardcoding what channels the bot can work in
	channels = ['testchannel']
	print(ctx.channel)
	if str(ctx.channel) in channels:
		print("in here")
		await ctx.send("hi")

		vid = "https://www.youtube.com/watch?v=73vP02w3mwo&list=RDv9M7g-nKMBU&index=48"
		start = vid.find('=')
		#print(vid[start+1:])
		tag = vid[start+1:]
		extended_loc = tag.find('&')
		if tag.find('&') != -1:
			tag = tag[:extended_loc]
		insertVideo(tag)
		#print(tag)		
		print('sucessful')

@client.command()
async def updatePlaylist(ctx):
	'''
	Takes all the youtube links in the discord channel and inserts them into the playlist
	'''
	#TODO: parse out any user messages after the link (e.x.) youtu.be/adfasdfa Yo this is a message
	#only works in these channels
	channels = ['testchannel', 'music-recommendations']
	print(ctx.channel)
	if str(ctx.channel) in channels:
		messages = 0
		#TODO: let the bot remember the last time it updated and use the after parameter on ctx.history
		async for message in ctx.history():
			if 'youtube.com' in message.content and 'playlist' not in message.content:
				#extract the video id from the url(i.e.) the characters after v= and before &
				start = message.content.find('=')
				print(message.content[start+1:])
				tag = message.content[start+1:]
				extended_loc = tag.find('&')
				if tag.find('&') != -1:
					tag = tag[:extended_loc]
				#TODO: add error checking for when a video can't be added
				insertVideo(tag)
				messages += 1
			elif 'youtu.be' in message.content:
				#extract the video url(i.e.) the characters after youtu.be/ and before ?
				start = message.content.find('be')
				tag = message.content[start+3:]
				extended_loc = tag.find('?')
				if tag.find('?') != -1:
					tag = tag[:extended_loc]
					print(tag)
				insertVideo(tag)
				messages += 1		
		await ctx.send('Successfully added {} songs to the playlist'.format(messages))

@client.command()
async def playlist(ctx):
	'''
	Sends the hardcoded playlist to the channel
	'''
	#TODO: try getting the playlistid from a json file instead
	channels = ['testchannel', 'music-recommendations']
	print(ctx.channel)
	if str(ctx.channel) in channels:
		await ctx.send("Here's the playlist of all the songs in this channel!\nhttps://www.youtube.com/playlist?list=PLEl38luv6tgnQvzjUKhLMUJr2jiB28gT4")

@client.command()
async def clearPlaylist(ctx):
	'''
	removes all the songs from the playlist
	'''
	channels = ['testchannel']

client.run('INSERT CLIENT ID HERE')