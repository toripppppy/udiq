import discord
from discord.ext import commands

from env.config import Config
from cogs import MainCog


config = Config()

TOKEN = config.token

bot = commands.Bot(
    command_prefix="udiq" + " ",
    intents=discord.Intents.all(),
    help_command=None
)

# setup cogs
@bot.event
async def setup_hook():
    await bot.add_cog(MainCog(bot))

def main():
    try:
        bot.run(TOKEN)
    finally:
        print("Log out : Udiq")

main()