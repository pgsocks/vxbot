import discord
from discord.ext import commands
import re

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

regex = re.compile(r"https?://twitter\.com/\S+")

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    if not "://twitter.com/" in message.content:
        return

    urls = "\n".join (
        url.replace("twitter.com", "vxtwitter.com")
        for url
        in regex.findall(message.content)
    )

    await message.reply("Friendly reminder to use vxtwitter!\n" + urls)
