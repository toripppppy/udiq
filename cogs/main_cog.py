"""
MainCog
Cog with basic features of Discord bot
"""

from discord.ext import commands

class MainCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# help
	@commands.command(name="help", brief="show help")
	async def help(self, ctx: commands.Context):
		await ctx.channel.send("here is help")

	# on ready
	@commands.Cog.listener()
	async def on_ready(self):
		print("On ready!")