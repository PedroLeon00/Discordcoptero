# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 13:44:12 2023

@author: Zuko
"""

import random

import discord


TOKEN = '*hay que escribir aquí el token, no puedo poner el mio pq discord identifica github como token filtrado*'
GUILD = '*Canal de discord*'
#hay que sustituir los *_* por el dato apropiado
intents = discord.Intents.default()
intents.members = True  # Habilitar el intent para miembros (solo si es necesario)
intents.messages = True  # Habilitar el intent para mensajes
intents.message_content = True #Habilitar la lectura de mensajes enviados 
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
        #se conecta a un server, lo comenta y dice el id del server
    
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    #comenta los usuarios del server



@client.event
async def on_member_join(member):
#cuando se una un miembro
    await member.create_dm()
    #crea un canal de texto
    await member.dm_channel.send(
    #manda un mensaje en dicho canal
        f'Holandaa {member.name}, welcome to the servidor!'
    )
    #await sirve para suspender la ejecución del resto de rutinas hasta que cada rutina se ha finalizado

@client.event
async def on_message(message):
    #cuando llegue un mensaje
    if message.author == client.user:
        return
    #con esto evitamos que el propio bot detecte su entrada de texto y entre en bucle

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    #Aquí defino una lista de referencias 

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
#envia mensaje aleatorio de la lista de referencias, await  pone en espera el resto de acciones
client.run(TOKEN)
