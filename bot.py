import discord
from discord import commands

client = commands.bot(command_prefix = "!")

@client.event
async def on_ready():
  print("Bot is online")
  
client.run("TOKEN")
