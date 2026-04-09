import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

# ===== BOT INFO =====
BOT_NAME = "DK Movie Bot 🎬"
OWNER_NAME = "DK Nabeel"
OWNER_USERNAME = "yourusername"

# ===== START IMAGE (FILE ID) =====
START_IMAGE = "PASTE_FILE_ID_HERE"

# ===== CHANNELS =====
FORCE_CHANNELS = ["channel1", "channel2"]
SOURCE_CHANNEL = -100xxxxxxxx
LOG_CHANNEL = -100xxxxxxxx

# ===== ADMIN =====
ADMINS = [123456789]

# ===== SETTINGS =====
AUTO_DELETE = 300
RESULTS_PER_PAGE = 5

START_MSG = f"""
👋 Welcome to {BOT_NAME}

🎬 Send movie name to search

👨‍💻 Developer: {OWNER_NAME}
📢 @{OWNER_USERNAME}
"""
