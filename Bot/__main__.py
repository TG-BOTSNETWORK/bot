import os
import asyncio
from sys import exit as SystemExit
from Bot import app
from Bot.logger import LOGGER
from pyrogram import idle

try:
    from config import API_ID, API_HASH, BOT_TOKEN
except ImportError:
    LOGGER.error("config.py not found or missing required variables!")
    raise SystemExit("Please ensure `config.py` exists and contains API_ID, API_HASH, BOT_TOKEN.")

from Bot.modules import load_modules
load_modules()

async def main():
    LOGGER.info("Starting Bot...")
    await app.start()
    LOGGER.info("Bot has started successfully!")
    print("Bot started successfully.")
    await idle()
    await app.stop()
    LOGGER.info("Bot has stopped.")

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        LOGGER.error("Bot stopped manually.")
    except SystemExit:
        LOGGER.error("System exit encountered.")
    except Exception as e:
        LOGGER.error(f"An unexpected error occurred: {e}")
        import sys
        sys.exit(1)