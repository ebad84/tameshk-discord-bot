import discord
import dotenv
import os




dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()





bannedlist=[]
banneds = open("banned.txt", "r")
for banned in banneds:
    bannedlist.append(banned)


@client.event
async def on_ready():
    print("connected")

@client.event
async def on_message(message):
    if str(message.author) in bannedlist:
        await message.delete()
    elif message.content == f"{prefix}لیست مسدودی":
        global bans
        bans=""
        for banned in bannedlist:
            bans = bans + "\n - "+banned

        if str(bans) != "":
            await message.reply(f"لیست کاربران مسدود شده:{bans}")
        else:
            await message.reply("خوشبختانه هیچ کاربری مسدود نشده است")
    

client.run(TOKEN)