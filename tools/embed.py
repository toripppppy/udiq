"""
Discord.py Embed creator
"""

import discord
from discord.ext import commands

COLOR_DICT = {
  "common": 0xF0F0FF,
  "warning": 0xFFFF00,
  "error": 0xFF0000,
  "success": 0x00FF00
}

def create_embed(color = "common", description = "") -> discord.Embed:
  embed = discord.Embed(title = "Udiq")
  
  if color in COLOR_DICT.keys():
    embed.color = COLOR_DICT[color]
  else:
    embed.color = COLOR_DICT["common"]
    raise ValueError(f"Warning: color '{color}' not found.")
  
  embed.description = description

  return embed


def create_help_embed(bot: commands.Bot):
  """
  create embed for "udiq help"
  """
  embed = create_embed()
  for command in bot.all_commands.values():
    # avoid hidden commands
    if command.hidden: continue

    name = bot.command_prefix + command.name
    if command.params:
      for param_name in command.params.keys():
        name += f" <{param_name}>"

    embed.add_field(name = name, value = command.brief, inline = False)

  return embed