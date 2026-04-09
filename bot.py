import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from config import *
from database import *

app = Client("movie_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ---------- FORCE SUB ----------
async def is_subscribed(client, user_id):
    if not FORCE_CHANNELS:
        return True   # skip force if empty

    for ch in FORCE_CHANNELS:
        try:
            member = await client.get_chat_member(ch, user_id)
            if member.status in ["kicked", "left"]:
                return False
        except:
            return False
    return True

def sub_buttons():
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(f"Join {ch}", url=f"https://t.me/{ch}")]
         for ch in FORCE_CHANNELS]
    )

# ---------- START ----------
@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id

    await users.update_one({"id": user_id}, {"$set": {"id": user_id}}, upsert=True)

    if not await is_subscribed(client, user_id):
        return await message.reply("⚠️ Join channels first!", reply_markup=sub_buttons())

    await message.reply_photo(
        photo=START_IMAGE,
        caption=START_MSG
    )

# ---------- SEARCH ----------
@app.on_message(filters.text & ~filters.command(["start"]))
async def search(client, message):
    user_id = message.from_user.id

    if not await is_subscribed(client, user_id):
        return await message.reply("⚠️ Join channels first!", reply_markup=sub_buttons())

    query = message.text.lower()

    results = []
    async for file in files.find({"name": {"$regex": query}}).limit(5):
        results.append(file)

    if not results:
        await requests.insert_one({"movie": query, "user": user_id})
        return await message.reply("❌ Not found. Request sent!")

    for file in results:
        msg = await message.reply_document(file["file_id"])

        await asyncio.sleep(AUTO_DELETE)
        await msg.delete()

# ---------- INDEX ----------
@app.on_message(filters.chat(SOURCE_CHANNEL) & filters.document)
async def index(client, message):
    await files.insert_one({
        "name": message.document.file_name.lower(),
        "file_id": message.document.file_id
    })

    await client.send_message(LOG_CHANNEL, f"Indexed: {message.document.file_name}")

# ---------- ADMIN ----------
@app.on_message(filters.command("stats") & filters.user(ADMINS))
async def stats(client, message):
    count = await users.count_documents({})
    await message.reply(f"👥 Users: {count}")

# ---------- RUN ----------
app.run()
