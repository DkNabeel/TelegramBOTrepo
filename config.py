import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

# ===== BOT INFO =====
BOT_NAME = "Movie Bot 🎬"
OWNER_NAME = "Zoro"
OWNER_USERNAME = "Zoro_Chaan"

# ===== START IMAGE (FILE ID) =====
START_IMAGE = "AgACAgUAAxkBAAIXSGnXWycPvjgpBNh1EVaQHL0JQVsNAALPEmsbQsjBVhjSlISWMNO2AQADAgADcwADOwQ"

# ===== CHANNELS =====
FORCE_CHANNELS = []
SOURCE_CHANNEL = -1003821671614
LOG_CHANNEL = -1003739583490

# ===== ADMIN =====
ADMINS = [8575439967]

# ===== SETTINGS =====
AUTO_DELETE = 300
RESULTS_PER_PAGE = 5

START_MSG = f"""
👋 Welcome to {BOT_NAME}

🎬 Send movie name to search

👨‍💻 Developer: {OWNER_NAME}
📢 @{OWNER_USERNAME}
"""
