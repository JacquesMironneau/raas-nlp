import discord
import os
from dotenv import load_dotenv
from ratio import phrase_to_ratio

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


async def handleSpecialMessages(message):
    if message.content == "!ping":
        await message.channel.send("pong uwu")
        return True
    if "!version" in message.content.lower():
        await message.channel.send("v1.4.1 ๐ค")
        return True
    goats = ["๐", "goat", "lionel", "messi", "cr7", "cristiano", "ronaldo"]
    if any(goat in message.content.lower() for goat in goats):
        await message.channel.send(file=discord.File('assets/siuu.gif'))
        return True
    return False
        
@client.event
async def on_message(message):
    if message.author == client.user and message.content.startswith("Et ce ratio"):
        await message.add_reaction("๐")
        await message.add_reaction("โค๏ธ")
        await message.add_reaction("๐")
        return
    elif message.author == client.user:
        return
    
    print("Received message: ", message.content)
    if await handleSpecialMessages(message):
        return

    ratio_phrase = phrase_to_ratio(message.content)
    if ratio_phrase != "":
        await message.channel.send(ratio_phrase)

@client.event
async def on_message_edit(before,after):
    if after.author == client.user:
        return
    ratio_phrase = phrase_to_ratio(after.content)
    if ratio_phrase != "":
        await after.channel.send(ratio_phrase)

@client.event
async def on_reaction_add(reaction, user):
    # send a message if every server member reacted to a message from the bot with a heart reactions
    if reaction.message.author == client.user and user != client.user and reaction.emoji == "โค๏ธ":
        users = [user async for user in reaction.users()]
        if len(users) / reaction.message.guild.member_count > 0.75:
            await reaction.message.channel.send(" j'ai dead รงa chakal ๐ฏ ๐ ๐ดโโ ๏ธ ๐คฃ")
            await reaction.message.channel.send(file=discord.File('assets/looser.gif'))
            
        
client.run(os.getenv("TOKEN"))