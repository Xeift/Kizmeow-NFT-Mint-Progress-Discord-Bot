import discord
import asyncio
import os
from discord.ext import commands
from discord_slash import SlashCommand
import urllib.request as ur
import json
import keep_alive

discord_token = os.environ['discord_token']#token

bot = commands.Bot(
	command_prefix="k!", #  bot prefix
	case_insensitive=True, #  case-sensitive
  intents=discord.Intents.all(), #  特權網關意圖(接收特殊事件)
  help_command=None #  禁用預設help指令
)
slash = SlashCommand(bot, sync_commands=True) 

@bot.event
async def on_ready():
  print("bot is online!")
  while True:
    file = open("config.json", "r")
    data = json.load(file)    
    if data['channel_id'] != None:
      channel_id = data['channel_id']
      contract_address = data['contract_address']
      total_supply = data['total_supply']
      etherscan_api_key = data['etherscan_api_key']
    
      url1='https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress='+contract_address+'&apikey='+etherscan_api_key #api url
      site1 = ur.urlopen(url1)
      page1 = site1.read()
      contents1 = page1.decode()
      data1 = json.loads(contents1)

      nowMint = data1['result']
    
      presence_ctx = "Mint progress: "+nowMint+"/"+total_supply
      await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=presence_ctx))
      channel=bot.get_channel(int(channel_id))
      await channel.edit(name=nowMint+"｜"+total_supply)
    await asyncio.sleep(60)

#Load Cog
extensions = [
	'cogs.ping',
  'cogs.config',
  'cogs.config_check'
]

if __name__ == '__main__':
	for extension in extensions:
		bot.load_extension(extension)  

keep_alive.keep_alive()
bot.run(discord_token)