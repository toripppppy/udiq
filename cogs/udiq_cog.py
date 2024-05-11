"""
UdiqCog

Cog for Udiq
"""

from discord.ext import commands
import random

from db.daos.knowledges_dao import KnowledgesDAO

class UdiqCog(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	# help
	@commands.command(name="random", brief="show random knowledge")
	async def random(self, ctx: commands.Context):
		knowledges = KnowledgesDAO().find_all()
		random_knowledge = random.choice(knowledges)
		await ctx.channel.send(random_knowledge)