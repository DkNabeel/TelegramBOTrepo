import os

API_ID = int(os.getenv("29489981"))
API_HASH = os.getenv("d06d320353dd369c577b33be893c622b")
BOT_TOKEN = os.getenv("8083538429:AAG49IcZunYqVyuqz_7S1ynKOvbRUR38OI4")
MONGO_URI = os.getenv("mongodb+srv://Nabeel: NPGzcTGYiqszW0j7y @cluster0.g5xiukh.mongodb.net/?appName=Cluster0")

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
