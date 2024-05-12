"""
UdiqCog

Cog for Udiq
"""

import discord
from discord.ext import commands
import random

from db.daos.knowledges_dao import KnowledgesDAO

class UdiqCog(commands.Cog):
	def __init__(self, bot: commands.Bot):
		super().__init__()
		self.bot = bot

		self.knowledges = KnowledgesDAO().find_all()

	@commands.Cog.listener()
	async def on_message(self, message: discord.Message):
		# avoid self message
		if message.author.bot: return

		for kn in self.knowledges:
			if kn.word in message.content:
				embed = discord.Embed(title=kn.word, description=kn.meaning)
				await message.channel.send("おっと、専門用語だよ。", embed=embed)
				return
		

	@commands.hybrid_command(name="random", description="random")
	async def random(self, ctx: commands.Context):
		knowledges = KnowledgesDAO().find_all()
		knowledge = random.choice(knowledges)

		embed = discord.Embed(title=knowledge.word, description=knowledge.meaning)

		await ctx.send(embed=embed, ephemeral=True)