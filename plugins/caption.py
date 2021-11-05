from pyrogram import Client, filters

import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

@Client.on_message(filters.reply & filters.text & ~filters.edited & ~filters.group & ~filters.command("deletethumbnail") & ~filters.command("mega_ini"))
async def newcap(_, message):
        await message.reply_text("Sorry! You are Banned!")
        return
    nc = message.reply_to_message
    if nc.media and not (nc.video_note or nc.sticker):
        await nc.copy(message.chat.id, caption=message.text)
