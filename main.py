import discord
from discord.ext import commands

import config
from cogs import MainCog, UdiqCog

bot = commands.Bot(
    command_prefix=config.BOT_PREFIX,
    intents=discord.Intents.all(),
    help_command=None
)

# setup cogs
@bot.event
async def setup_hook():
    await bot.add_cog(MainCog(bot))
    await bot.add_cog(UdiqCog(bot))

def main():
    bot.run(config.TOKEN)

main()