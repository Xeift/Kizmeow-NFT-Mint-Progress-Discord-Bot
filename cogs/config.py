import discord
import asyncio 
from discord_slash.utils.manage_commands import create_option
import urllib.request as ur
import json
from discord_slash import cog_ext
from core.cog_core import cogcore
import os
import time

class config_check(cogcore):
  @cog_ext.cog_slash(
  name="config_check",
  description="[admin] check the information you entered")

  async def config(self,ctx):
    role = discord.utils.get(ctx.guild.roles, name="Bot Admin")
    if role in ctx.author.roles:
      await ctx.send(file=discord.File("config.json"))

    else:
      embed=discord.Embed(title="[failed]\nreason: user do not have `Bot Admin` role", color=0xe8006f)
      await ctx.send(embed=embed)   
def setup(bot):
  bot.add_cog(config_check(bot))