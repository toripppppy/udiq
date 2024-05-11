"""
Bot Config
"""

from dotenv import load_dotenv
import os

load_dotenv()

# Setting
BOT_PREFIX = "udiq" + " "

# from .env
TOKEN = os.getenv("TOKEN")
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")