"""
UdiqCog

Cog for Udiq
"""

import discord
from discord.ext import commands
import random

from db.controllers.knowledges_controller import KnowledgesController
from db.models.knowledge_model import KnowledgeModel
from tools.parser import Parser
import config

class UdiqCog(commands.Cog):
	def __init__(self, bot: commands.Bot):
		super().__init__()
		self.bot = bot
		self.knowledges_controller = KnowledgesController()
		self.knowledges = self.knowledges_controller.find_all()

	@commands.Cog.listener()
	async def on_message(self, message: discord.Message):
		# avoid self message
		if message.author.bot: return

		parser = Parser()
		message_words = parser.get_words(message.content)

		for kn in self.knowledges:
			if kn.word in message_words:
				embed = discord.Embed(title=kn.word, description=kn.meaning)
				await message.channel.send("おっと、専門用語だよ。", embed=embed)
				return

	@commands.hybrid_command(name="random", description="random")
	async def random(self, ctx: commands.Context):
		knowledges = self.knowledges_controller.find_all()
		knowledge = random.choice(knowledges)

		embed = discord.Embed(title=knowledge.word, description=knowledge.meaning)

		await ctx.send(embed=embed, ephemeral=True)

	@commands.hybrid_command(name="add", description="add new knowledge")
	async def add(self, ctx: commands.Context):
		
		args = ctx.message.content.replace(config.BOT_PREFIX + "add ", "").split()
		print(args)
		if len(args) == 2:
			new_knowledge = KnowledgeModel(*args)
			print(new_knowledge)
			self.knowledges_controller.insert_one(new_knowledge)

		# update local knowledges
		self.knowledges = self.knowledges_controller.find_all()

		embed = discord.Embed(
			title=f"Added \"{new_knowledge.word}\"",
			description=f"{new_knowledge.word}:\n{new_knowledge.meaning}"
		)

		await ctx.send(embed=embed, ephemeral=True)