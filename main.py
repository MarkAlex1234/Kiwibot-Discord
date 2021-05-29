import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
#from replit import db -WIP


client = discord.Client()

def get_helpList():
  printHelpList = """Kiwibot currently has these commands:
  
  #hello - Kiwibot says hello!
  #movie - Kiwibot suggests a random movie to watch!
  #youtube - Kiwibot suggests a random youtube video to watch!
  #ship - Kiwibot ships two people together! 
  #clips - Kiwibot displays a list of audio clips!
  """
  return(printHelpList)

def get_movie():
  randomMovie = random.randint(1,1000)
  randomMovie = str(randomMovie)
  
  response = requests.get("https://api.themoviedb.org/3/movie/"+randomMovie+"?api_key=5495465db3896a59f84193b0784143e6&language=en-US")
  print('successfully requested movie')
  json_data = json.loads(response.text)
  movie =json_data['title'] + ": " + json_data['overview']
  return(movie)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('#help'):
          printHelpList = get_helpList()
          await message.channel.send(printHelpList)

        if message.content.startswith('#hello'):
            await message.channel.send('Hello!')
        
        if message.content.startswith('#movie'):
            movie = get_movie()
            await message.channel.send(movie)

     
keep_alive()
client.run(os.getenv('TOKEN'))
