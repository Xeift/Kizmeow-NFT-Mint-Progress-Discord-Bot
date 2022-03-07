import discord
import asyncio 
from discord_slash.utils.manage_commands import create_option
import urllib.request as ur
import json
from discord_slash import cog_ext
from core.cog_core import cogcore
import os
import time

class config(cogcore):
  @cog_ext.cog_slash(
  name="config",
  description="[admin] setup the bot",
  options=
  [
    create_option
    (
      name="channel_id",
      description="the voice channel you want bot to display mint progress",
      option_type=3,
      required=True
    ),
    create_option
    (
      name="contract_address",
      description="the contract address of your NFT project",
      option_type=3,
      required=True
    ),
    create_option
    (
      name="total_supply",
      description="the total supply of your NFT project",
      option_type=3,
      required=True
    ),
    create_option
    (
      name="etherscan_api_key",
      description="your etherscan api key",
      option_type=3,
      required=True
    )
  ]
  )

  async def config(self,ctx,channel_id,contract_address,total_supply,etherscan_api_key):
    role = discord.utils.get(ctx.guild.roles, name="Bot Admin")
    if role in ctx.author.roles:

      file = open("config.json", "r")
      data = json.load(file)

      data['channel_id'] = channel_id
      data['contract_address'] = contract_address
      data['total_supply'] = total_supply
      data['etherscan_api_key'] = etherscan_api_key
      
      with open('config.json', 'w') as outfile:
        json.dump(data, outfile)
        
      embed=discord.Embed(title="[sucess]\ntype `/config_check` to check config", color=0x00ff00)
      await ctx.send(embed=embed) 

    else:
      embed=discord.Embed(title="[failed]\nreason: user do not have `Bot Admin` role", color=0xe8006f)
      await ctx.send(embed=embed)   
def setup(bot):
  bot.add_cog(config(bot))