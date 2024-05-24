"""
embed

some tools for embed
"""

import discord

COLOR_DICT = {
  "white": 0xF0F0FF,
  "yellow": 0xFFFF00,
  "red": 0xFF0000,
  "green": 0x00FF00
}

def create_delete_embed(response: dict):
	if response["code"] == "success":
		return discord.Embed(
			color=COLOR_DICT["green"],
			title="udiq delete",
			description=f"\"{response['word']}\"を正常に削除しました。"
		)

	elif response["code"] == "error.notfound":
		return discord.Embed(
			color=COLOR_DICT["red"],
			title="削除失敗",
			description=f"\"{response['word']}\"が見つかりませんでした。"
		)
	
	elif response["code"] == "error.invalid":
		return discord.Embed(
			color=COLOR_DICT["red"],
			title="形式が不正です",
			description=f"コマンドの形式が異なります。\nudiq delete <word>"
		)
	
def create_add_embed(response: dict):
	if response["code"] == "success":
		return discord.Embed(
			color=COLOR_DICT["green"],
			title="udiq add",
			description="新しい単語を追加しました。\n" + response['word'] + " : " + response['meaning']
		)
	
	elif response["code"] == "error.invalid":
		return discord.Embed(
			color=COLOR_DICT["red"],
			title="形式が不正です",
			description=f"コマンドの形式が異なります。\nudiq add <word> <meaning>"
		)