import hydrogram
from pyrogram import Client
from pyrogram import idle
from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN
)
app = Client(
    "restrict bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)