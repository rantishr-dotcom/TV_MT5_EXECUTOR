
import os
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_TOKEN = os.getenv("WEBHOOK_TOKEN", "tv_mt5_secret")

LIVE_TRADING = os.getenv(
    "LIVE_TRADING",
    "false"
).lower() == "true"
