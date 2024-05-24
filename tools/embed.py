"""
embed

some tools for embed
"""

import discord
from discord.ext import commands

COLOR_DICT = {"white": 0xF0F0FF, "yellow": 0xFFFF00, "red": 0xFF0000, "green": 0x00FF00}


def create_help_embed(bot: commands.Bot) -> discord.Embed:
    embed = discord.Embed()
    for command in bot.all_commands.values():
        # avoid hidden commands
        if command.hidden:
            continue
        name = bot.command_prefix + command.name
        if command.params:
            for param_name in command.params.keys():
                name += f" <{param_name}>"

        embed.add_field(name=name, value=command.brief, inline=False)

    return embed


def create_delete_embed(response: dict) -> discord.Embed:
    if response["code"] == "success":
        return discord.Embed(
            color=COLOR_DICT["green"],
            title="udiq delete",
            description=f"\"{response['word']}\"を正常に削除しました。",
        )

    elif response["code"] == "error.notfound":
        return discord.Embed(
            color=COLOR_DICT["red"],
            title="削除失敗",
            description=f"\"{response['word']}\"が見つかりませんでした。",
        )

    elif response["code"] == "error.invalid":
        return discord.Embed(
            color=COLOR_DICT["red"],
            title="形式が不正です",
            description=f"コマンドの形式が異なります。\nudiq delete <word>",
        )


def create_add_embed(response: dict) -> discord.Embed:
    if response["code"] == "success":
        return discord.Embed(
            color=COLOR_DICT["green"],
            title="udiq add",
            description="新しい単語を追加しました。\n\n"
            + response["word"] + " : " + response["meaning"],
        )

    elif response["code"] == "error.invalid":
        return discord.Embed(
            color=COLOR_DICT["red"],
            title="形式が不正です",
            description=f"コマンドの形式が異なります。\nudiq add <word> <meaning>",
        )


def create_list_embed(response: dict) -> discord.Embed:
    if response["knowledges"] is None:
        return discord.Embed(
            title="単語が登録されていません",
            description="udiqに単語データが見つかりませんでした。\n新しい単語を登録したい場合は、\nudiq add <word> <meaning>\nで登録できます。",
        )
    else:
        desc = ""
        for kn in response["knowledges"]:
            desc += kn.word + " : " + kn.meaning + "\n"

        return discord.Embed(
            title="udiq list",
            description=desc
        )
