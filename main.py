import discord
import os
import requests
import json
import random
from replit import db
from keepalive import keep_alive


client = discord.Client()

cinetxt = open("cine.txt", "r")
cine_list = cinetxt.read()
cine=cine_list.split("\n")
cinetxt.close()

fazetxt = open("faze.txt", "r")
faze_list = fazetxt.read()
faze = faze_list.split("\n")
fazetxt.close()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('cine'):
    if("cinenew" in message.content.lower()):
      cinenou = message.content.split("cinenew ", 1)[1]
      if cinenou in cine:
        await message.channel.send('Il stiu pe asta lol')
      else:
        cine.append(cinenou)
        cinetxt = open("cine.txt", "a")
        cinetxt.write("\n")
        cinetxt.write(cinenou)
        await message.channel.send("Notat")
    else:
      await message.channel.send(random.choice(cine))

  if message.content.startswith('faze'):
    if("fazehelp" in message.content.lower()):
      await message.channel.send('Comenzi Faze Dulci Alex Bittman:')
      await message.channel.send('"faze" - Iti zic de bine')
      await message.channel.send('"cine" - Iti raspund la intrebari ce incep cu "cine"')
      await message.channel.send('"cinenew" - Adaugi nume noi la lista de bazati (exemplu: cinenew Gigi Becali')
      await message.channel.send('"fazehelp" - Iti zic ce poti face cu botul (ca acum)')
      await message.channel.send('"fazenew" - Adauga o faza noua la lista de faze (exemplu: fazenew Buna dimineata! Cafelutsa e servita)')
      await message.channel.send('"fazeinvite - Iti dau link-ul meu sa ma bagi la tine pe server"')
      await message.channel.send('"fazesource" - Iti dau link-ul de la codul meu sursa')
      await message.channel.send('"eurotranslate" - Iti traduc orice propozitie in limba lui OG Eastbull (coming soon)')
    elif("fazenew" in message.content.lower()):
      fazanoua = message.content.split("fazenew ",1)[1]
      if fazanoua in faze:
        await message.channel.send('O stiu pe asta lol')
      else:
        faze.append(fazanoua)
        fazetxt = open("faze.txt", "a")
        fazetxt.write("\n")
        fazetxt.write(fazanoua)
        fazetxt.close()
        await message.channel.send('Buna faza Tugay')
    elif("fazeinvite" in message.content.lower()):
      await message.channel.send('https://discord.com/oauth2/authorize?client_id=860255482828947466&permissions=0&scope=bot')
    elif("fazesource" in message.content.lower()):
      await message.channel.send('https://replit.com/@RdukuChef/FazeComiceAlexBittman?v=1')
    else:
      await message.channel.send(random.choice(faze))

  #if message.content.startswith('eurotranslate'):
    #euro = message.content.split("eurotranslate ", 1)[1]
    #for iterator in range (0, len(euro)):
      #if euro[iterator] in [' ', '.', '?', '!']:
        #continue
      #euro[iterator]='€'

    
keep_alive()
client.run(os.getenv('TOKEN'))
