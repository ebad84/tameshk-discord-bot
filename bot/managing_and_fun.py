import discord
from discord.ext import commands
import os
import random
import PersianSwear
#insert your admins here
admins=["SMM#9107","NGP#9847","@HADI#0001","@Amir14#6843"]
TOKEN = os.getenv('DISCORD_TOKEN')
bot=commands.Bot(command_prefix="tdb.")
ps=PersianSwear.PersianSwear()


@bot.event
async def on_ready():
    print("connected")
@bot.command()
async def update(ctx):
  if str(ctx.message.author) in admins:
    ps.update()
    await ctx.reply("update shod")
  else:
    embed=discord.Embed(title="خطا", description="شما ادمین نیستید :)", color=0xFF0000)
    embed.set_image(url="https://s.keepmeme.com/files/en_posts/20210512/black-guy-smiles-at-camera-poker-face-meme.jpg")
    await ctx.reply(embed=embed)
  
@bot.event
async def on_message(message):
  await bot.process_commands(message)
  mention=message.author.mention
  if ps.has_swear(str(message.content).replace("|","")) and not message.author == bot.user:
    filtered_message=ps.filter_words(str(message.content).replace("|",""))
    embed=discord.Embed(title="ادب مرد به از دولت اوست...",description=f"پیام از طرف {mention}\n{filtered_message}")
    embed.set_footer(text="لطفا مودب باشید\nمسیج شما به ادمین ها ارسال شد\nاگه فکر می کنید اینکه بات یه کلمه رکیک تو مسیج شما تشخیص داده یه باگه یا لازم نیست این کلمه به عنوان یه کلمه رکیک تشخیص داده بشه یه تیکت باز کنید و به ادمین ها اطلاع بدید")
    embed.set_image(url="https://c.tenor.com/y6lfLkr_aOQAAAAM/justin-timberlake-smh.gif")
    await message.delete()
    await message.channel.send(embed=embed
    )
    channel=bot.get_channel(855075598812184577)
    await channel.send(f"ye band khodaee fosh dad\nin mantioneshe:{mention}\nin ham message:\n{message.content}")



  elif message.content == "sghl":
    await message.reply("منظورت سلام بود؟")
  elif message.content == "سلام" and message.author != bot.user:
    hellos = (f"و علیکم السلام بر {message.author.mention} عزیز!:wave:",
             f"و علیکم السلام!👋حالت چطوره؟",
              f"سلام علیکم")
    response = random.choice(hellos)
    await message.reply(response)
  elif message.content == "خداحافظ" or message.content == "خدانگهدار":
    byes=['خدانگهدار👋👋','خداحافظظظظ👋👋👋','به امید دیدار☺😉','خوش حال شدم از دیدنت، خدانگهدار','خداحافظ']
    bye = random.choice(byes)
    await message.reply(bye)
  
  

bot.run(TOKEN)