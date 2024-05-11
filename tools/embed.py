"""
Discord.py Embed creator
"""

import discord

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