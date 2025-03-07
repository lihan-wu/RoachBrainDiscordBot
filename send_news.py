import discord
from discord.ext import commands
import feedparser
import re
import os
import os.path
import time
import threading
from dotenv import load_dotenv

load_dotenv()

def close_bot():
    time.sleep(10)
    print("script completed. closing in 5 seconds")
    time.sleep(5)
    os._exit(0)

CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

def get_news_feed(url):
    news_data = []
    news_feed = feedparser.parse(url)
    entry = news_feed.entries[0]
    news_data.append(entry.title)
    news_data.append(entry.links[0]["href"])
    try:
        news_data.append(entry.links[1]["href"])
    except:
        news_data.append(None) 
    cleaned_summary = cleanhtml(entry.summary)
    cleaned_summary_trunc = (cleaned_summary[:1000] + '...') if len(cleaned_summary) > 1000 else cleaned_summary
    news_data.append(cleaned_summary_trunc)
    news_data.append(entry.published)
    return news_data

close_bot_thread = threading.Thread(target=close_bot)

close_bot_thread.start()

post_data = get_news_feed('https://store.steampowered.com/feeds/news/app/1422450/?cc=US&l=english')

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.event
async def on_ready():
    if os.path.isfile('./previous_post.txt') == False:
        previous_post = open('./previous_post.txt', "w")
        previous_post.write(post_data[0])
    if open('./previous_post.txt', 'r').read() == post_data[0]:
        return 
    elif open('./previous_post.txt', 'r').read() != post_data[0]:
        channel = bot.get_channel(1087390002243190864)
        embed = discord.Embed(
            title=post_data[0],
            url=post_data[1],
            color=discord.Colour.greyple()
        )

        embed.set_thumbnail(url=post_data[2])
        embed.add_field(
            name=post_data[4],
            value=post_data[3],
            inline=False
        )

        previous_post = open('./previous_post.txt', "w")
        previous_post.write(post_data[0])

        await channel.send(f'<@&1254645811225165916> {post_data[0]}')
        await channel.send(embed=embed)
    

discord_api_key = os.getenv('discord_api_key')

bot.run(discord_api_key)