# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:32:40 2023

@author: Zuko
"""



import discord 

#dotenv es una biblioteca para cargar variables de entorno desde un archivo ".env"
#load_dotoenv es una función proporcionada por el módulo "dotenv"

TOKEN='MTE1MDc5OTk4NTY1MTIyODczMg.GL1udS.0g1WOt4_gh8ZO_4uJ1-trSFAV4GBtJyALYODDQ'
#carga cosas .env

#os.getenv es una función de módulo os y getenv es... vas a flipar, obtener env
#la movida es qué es discord token, PREGUNTAR A RUBEN
intents = discord.Intents.default()
intents.typing = False
#parece que hay que definir los intents del cliente, pq es true or false tengo que trabajarlo
client = discord.Client(intents=intents)

@client.event
#esto le indica al programa que la funcion que ocurre es un manejador de eventos relacionado con el bot
async def on_ready():
    #esto indica que acción va a ocurrir cuando "on_ready"
    print(f'{client.user.name} has connected to Discord!')
    #client.user es el nombre de usuario del cliente, el bot
client.run(TOKEN)  
    #esta linea inicia la ejecución del cliente de ds utilizando el token proporcionado  