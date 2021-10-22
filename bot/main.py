import discord
import os
from khayyam import JalaliDatetime
from live import alive
from discord.ext import commands
import random
from discord.ext import tasks
from googletrans import Translator
colors=[0x1d8ddb,0x2c3157,0xd44492,0xbd3787,0x8a375,0x42ae4d,0x106939]
import requests
import contextlib
import io
#Create googletrans instance
translator = Translator()
#turn on a option for debug
translator.raise_Exception = True
#insert your admins here
admins=["SMM#9107","NGP#9847","@HADI#0001","@Amir14#6843"]
#help text embed
help_embed = discord.Embed(title="راهنمای دستورات بات <:logo:839559626265329704>:",description="""
***تمامی دستورات با ***`.tdb`*** آغاز می شوند***
<:logo:839559626265329704>`help,h,راهنما` : نمایش راهنما \n========
<:logo:839559626265329704>`account` : مشاهده اطلاعات اکانت دیسکورد  \n========
<:logo:839559626265329704>`ping` : دریافت میزان تاخیر ربات \n========
""", color=0xffffff)
#create discord.py instance
bot = commands.Bot(command_prefix="tdb.")
bot.remove_command('help')
#create token varaible 
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()

golds={}
golds= requests.get(url="http://nimagp.pythonanywhere.com").json()
@tasks.loop(seconds = 30)
async def update():
  golds= requests.get(url="http://nimagp.pythonanywhere.com").json()
update.start()
def add_gold():
    random_id=random.choice(list(golds.keys()))
    txt = f'''\n\n\n> _{golds[random_id]["gold speaker"]}_\n> "_{golds[random_id]["gold"]}_"'''
    return txt
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="tdb.help"))
    print(f"Logged in as {bot.user.name}({bot.user.id}")


@bot.command(help='پینگ ربات')
async def ping(ctx):
    await ctx.reply(f"پونگ! `{str(round(bot.latency * 1000))}` میلی ثانیه")
@bot.command(name="help",help="نمایش راهنما",aliases=["h","راهنما"])
async def help(ctx):
    await ctx.reply(embed=help_embed)

async def bot_is_online(ctx):
  if str(ctx.message.author) in admins:
    channel = bot.get_channel(870624299877277716)
    embed=discord.Embed(title=f"ربات روشن شد!", description="هم اکنون میتوانید از ربات استفاده کنید", color=0x00ff00)
    await channel.send(embed=embed)
    embed=discord.Embed(title="انجام شد", description="همگان دانند وضعیت مرا :)", color=0x00ff00)
    await ctx.reply(embed=embed)
  else:
    embed=discord.Embed(title="خطا", description="شما ادمین نیستید :)", color=0xFF0000)
    embed.set_image(url="https://s.keepmeme.com/files/en_posts/20210512/black-guy-smiles-at-camera-poker-face-meme.jpg")
    await ctx.reply(embed=embed)


@bot.command()
async def account(ctx):
  global nickname
  if ctx.message.author.display_name  == "None":
    nickname = "هنوز برای خود نام مستعاری تنظیم نکرده اید!"
  else:
    nickname = ctx.message.author.display_name


  embed=discord.Embed(title='**🔰اطلاعات اکانت دیسکورد شما🔰**', description=f"نام کاربری:\n*`{ctx.message.author.name}`*\n-----\nنام مستعار:\n*`{nickname}`*\n-----\nآیدی عددی:\n*`{ctx.message.author.id}`*\n-----\nمنشن:\n{ctx.message.author.mention}",color=random.choice(colors))
  embed.set_image(url="https://images.hamshahrionline.ir/images/2013/5/13-5-12-1018583-1.jpg")
  await ctx.send(embed=embed)


@bot.command()
async def youtube(ctx):
  if "team" in [y.name.lower() for y in ctx.message.author.roles]:
    day=JalaliDatetime.now().strftime('%A')
    embed=discord.Embed(title="و ای عزیزانم",description=f'امروز نوبت {os.getenv(day)} هست',color=random.choice(colors))
    if not os.getenv(day) == "تعطیلی":
      embed.set_image(url="https://memegenerator.net/img/instances/85686779/heres-your-youtube-turn.jpg")
    await ctx.send(embed=embed)
  else:
    embed=discord.Embed(title="خطا",description="من از اختاپوس می پرسم تو جزو اعضای تیم تمشکی؟",color=0xFF0000)
    embed.set_image(url="https://i.kym-cdn.com/photos/images/facebook/000/871/268/979.png")
    await ctx.send(embed=embed)



@bot.command()
async def t2en(ctx,* , text):
  translated_text=translator.translate(text,src='fa',dest='en').text
  msg=f'ترجمه متن مورد نظر:\n{translated_text}'
  embedd=discord.Embed(title="ترجمه شد",description=msg+add_gold(),color=random.choice(colors))
  await ctx.reply(embed=embedd)


@bot.command()
async def t2fa(ctx,* ,text):
  translated_text=translator.translate(text,src='en',dest='fa').text
  msg=f'ترجمه متن مورد نظر:\n{translated_text}'
  embedd=discord.Embed(title="ترجمه شد",description=msg+add_gold(),color=random.choice(colors))
  await ctx.reply(embed=embedd)


@bot.command()
async def run_code(ctx, *,commands=None):
  if str(ctx.message.author) in admins:
    if not commands:
      embed=discord.Embed(title="خطا",description="منو سرکار گذاشتی یا خودتو که کامند میزنی ولی دستور نمیدی؟",color=0xFF0000)
      embed.set_image(url="https://cdn.thingiverse.com/assets/83/5c/96/ee/81/featured_preview_Crm4_G3uns8_1.jpg")
      await ctx.reply(embed)

    str_obj = io.StringIO() #Retrieves a stream of data
    try:
      with contextlib.redirect_stdout(str_obj):
        exec(commands)
      output=str_obj.getvalue()  
    except Exception as error:
      output=f"ارور داد :( :\n{error}"
    embed=discord.Embed(title="ران شد :)",description=f"بیا اینم نتیجه:\n{output}",color=random.choice(colors))
    await ctx.reply(embed=embed)

    
  else:
    embed=discord.Embed(title="خطا", description="شما ادمین نیستید :)", color=0xFF0000)
    embed.set_image(url="https://s.keepmeme.com/files/en_posts/20210512/black-guy-smiles-at-camera-poker-face-meme.jpg")
    await ctx.reply(embed=embed)

@bot.command()
async def send(ctx,*,message):
  if not str(ctx.message.author) in admins:
    embed=discord.Embed(title="خطا", description="شما ادمین نیستید :)", color=0xFF0000)
    embed.set_image(url="https://s.keepmeme.com/files/en_posts/20210512/black-guy-smiles-at-camera-poker-face-meme.jpg")
    await ctx.reply(embed=embed)
  if not ctx.message.reference:
    await ctx.message.delete()
    await ctx.send(message)
  else:
    await ctx.message.delete()
    ref = await ctx.channel.fetch_message(ctx.message.reference.message_id)
    await ref.reply(message)
@bot.command()
async def announce(ctx,*,message):
  if not str(ctx.message.author) in admins:
    embed=discord.Embed(title="خطا", description="شما ادمین نیستید :)", color=0xFF0000)
    embed.set_image(url="https://s.keepmeme.com/files/en_posts/20210512/black-guy-smiles-at-camera-poker-face-meme.jpg")
    await ctx.reply(embed=embed)
  else:
    await ctx.reply("پیام به چنل انانسمنت سرور کامیونیتی ارسال شد!")
    announce_channel = bot.get_channel(871708836153679892)
    await announce_channel.send(ctx.content)





alive()
bot.run(TOKEN)