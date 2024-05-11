"""
Load config from .env
"""

from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = str(os.getenv("TOKEN"))
LOG_CHANNEL_ID = str(os.getenv("LOG_CHANNEL_ID"))