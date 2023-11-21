import discord
import os
import json
import requests
from replit import db #yeh just do this proragram in replit
import random

# client = commands.Bot(command_prefix='.')
client = discord.Client()


love_words = ['neko','cat','meow','like','love','desu']
anime_life = ['cats are cute :3',                   #random choice make sure they are one separate line
            'anime is love',
            'neko para is a visual novel',
            'i love anime',
            'hai']
    
def get_quote():
    response = requests.get('https://animechan.vercel.app/api/random')
    json_data = json.loads(response.text)
    
    quote=json_data['anime']        # finally after so much time there are other ways to di but this is the easiet took quite a long time
    return quote
def update_animeenc(anime_message):
        
    if "animeenc" in db.keys():
        animeenc = db["animeenc"]
        animeenc.append(anime_message)      # append is () not [] took me an hours to realise that mistake
        db["animeenc"] = animeenc  
    else:
        db["animeenc"] = [anime_message]
    
def delete_animeenc(index):
    animeenc = db["animeenc"]

    if len(animeenc)>index:
        del animeenc[index]
        db["animeenc"] = animeenc
        
@client.event
async def on_ready():
    print("Hello I am Hime")
    
@client.event
async def on_message(message):
    msg = message.content

    if message.content.startswith('anime'):
        quote = get_quote()
        await message.channel.send(quote)
    
    
    if message.content.startswith("blue"):
        await message.channel.send("oceans are blue")
    
    
    options = anime_life
    if "animeenc" in db.keys():
        options = options.extend(db["animeenc"])
    
    if any(word in msg for word in love_words):
        await message.channel.send(random.choice(options))

    if msg.startswith("new"):
        anime_message = msg.split("new",1)[1]
        update_animeenc(anime_message)
        await message.channel.send("New quote added")
    
    if msg.startswith("del"):
        animeenc= []
        if "animeworld" in db.keys():
            index = int(msg.split("del",1)[1])
            delete_animeenc(index)
            animeenc = db["animeenc"]
        await message.channel.send(animeenc)




client.run(os.getenv('TOKEN'))  #very useful to hide the data

