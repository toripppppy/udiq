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
import tools.embed
import config

class UdiqCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot
        self.knowledges_controller = KnowledgesController()
        self.knowledges = self.knowledges_controller.find_all()

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # avoid if knowledges is empty
        if self.knowledges is None: return
        # avoid self message
        if message.author.bot: return
        # avoid commands
        ctx = await self.bot.get_context(message)
        if ctx.command is not None: return

        parser = Parser()
        message_words = parser.get_words(message.content)
        
        for kn in self.knowledges:
            if kn.word in message_words:
                embed = discord.Embed(title=kn.word, description=kn.meaning)
                await message.channel.send("おっと、専門用語だよ。", embed=embed)
                return

    @commands.command(name="random", brief="show random word from udiq")
    async def random(self, ctx: commands.Context):
        knowledges = self.knowledges_controller.find_all()
        knowledge = random.choice(knowledges)

        embed = discord.Embed(title=knowledge.word, description=knowledge.meaning)

        await ctx.send(embed=embed)

    @commands.command(name="add", brief="add new knowledge")
    async def add(self, ctx: commands.Context):
        args = ctx.message.content.replace(config.BOT_PREFIX + "add ", "").split()
        res = {}
        if len(args) == 2:
            new_knowledge = KnowledgeModel(*args)
            res["code"] = self.knowledges_controller.insert_one(new_knowledge)
            res["word"] = new_knowledge.word
            res["meaning"] = new_knowledge.meaning
        else:
            res["code"] = "error.invalid"

        # update local knowledges
        self.knowledges = self.knowledges_controller.find_all()

        embed = tools.embed.create_add_embed(res)

        await ctx.send(embed=embed)
        
    @commands.command(name="list", brief="show list of knowledges")
    async def _list(self, ctx: commands.Context):
        res = {}
        res["knowledges"] = self.knowledges_controller.find_all()
        embed = tools.embed.create_list_embed(res)

        await ctx.send(embed=embed)
    
    @commands.command(name="delete", brief="delete specified knowledge")
    async def delete(self, ctx: commands.Context):
        args = ctx.message.content.replace(config.BOT_PREFIX + "delete ", "").split()
        res = {}
        if len(args) == 1:
            res["code"] = self.knowledges_controller.delete_one(args[0])
            res["word"] = args[0]

            # update local knowledges
            self.knowledges = self.knowledges_controller.find_all()
        else:
            # invalid command
            res["code"] = "error.invalid"

        embed = tools.embed.create_delete_embed(res)
        await ctx.send(embed=embed)