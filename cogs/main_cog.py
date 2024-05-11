"""
MainCog

Cog with basic features of Discord bot
"""

from discord.ext import commands

import config
import tools

class MainCog(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	# help
	@commands.command(name="help", brief="show help")
	async def help(self, ctx: commands.Context):
		await ctx.send(embed=tools.create_help_embed(self.bot))

	# on ready
	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.bot.user.name}: I'm ready!")

		log_channel = await self.bot.fetch_channel(config.LOG_CHANNEL_ID)
		await log_channel.send(f"{self.bot.user.name}: I'm ready!")