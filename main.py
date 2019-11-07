import asyncio
import discord
import datetime
import os
from discord import Emoji
from discord.utils import get
from discord.ext import commands

from webserver import keep_alive


client = discord.Client()

token = "NjM5MTgxODc1NDkxMTEwOTIy.XbnlgQ.UDDkYT7yQN2Nob6g3V7bnR8J0JQ"


@client.event
async def on_ready():
    print("Logged in as ") 
    print(client.user.name)
    print(client.user.id)
    print("===========")
    
    await client.change_presence(activity=discord.Activity(name="!김민-----김민AI실행",type = 1))

@client.event
async def on_message(message):
    if message.author.bot:
        return None 


    if message.content.startswith('!김민'): 
      await message.channel.send('왜? 뭐 도와줄까?\n명령어 목록 - !김민 명령어')

    if message.content.startswith('!김민 병신'): 
      await message.channel.send('예')

    if message.content.startswith('!김민 명령어'): 
      await message.channel.send('!김민 숫자세봐 \n!김민 너는 뭐니 \n!김민 병신')

    if message.content.startswith('!김민 숫자세봐'): 
        for i in range(10):
          await message.channel.send('i+1')

    if message.content.startswith('!김민 너는 뭐니'): 
      await message.channel.send("나는 김민봇, 저는 사실 할줄아는게 숫자세는것 밖에 없어요")
        

client.run(token)

