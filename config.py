import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_ID = os.getenv("API_ID", "27805819")
API_HASH = os.getenv("API_HASH", "7372a27cd4dc20b792bb117b038db7ef")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7481943486:AAEWhDdfqQEE9SA3vBQb4MZ_MsM8p3hgSVc")