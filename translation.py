from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
<b>Hey</b> {}

<b>I am Mega Link Downloader bot !</b>

<b>Just Send me Mega.nz link and I will return in File or Video For You !</b>

<b>✪ I can set custom captions and custom thumbnails too!</b>

<b>✪ I can also download links which are bigger than 2GB By Splitting It !</b>

<b>Use Help Command to know how to use me !</b>

<b><b>✪ <b>Made With 💕 By</b> <b>@Tellybots_4u</b>
"""
    HELP_TEXT = """
<b>Just Send Me Mega.nz link to Get Started</b>

📝 <b>Folder links are not supported.</b>

📒 <b>Your link should be valid(not expired or been removed) and should not be password protected or encrypted or private!</b>

✪ <b>If you want a custom thumbnail for your uploads send a photo before sending the mega link!.</b>

✪ <b> It means it is not necessary to send an image to include as an thumbnail.
If you don't send a thumbnail the video/file will be uploaded with an auto genarated thumbnail from the video.
The thumbnail you send will be used for your next uploads!</b>

✪ <b>Use /deletethumbnail command if you want to delete the previous saved thumbnail.
(Then the video will be uploaded with an auto-genarated thumbnail!)</b>

✪ <b>Special Features</b> :- <b>Set caption to any file you want!</b>
"""
    ABOUT_TEXT = """
<b>🤖 My Name : Mega Link Uploader Bot</b>\n
<b>🚦 Version : <a href='https://telegram.me/tellybots_4u'>2.0</a></b>\n
<b>💫 Source Code : <a href='https://t.me/tellybots_digital'>Click Here</a></b>\n
<b>🗃️ Library : <a href='https://pyrogram.org'>Click Here</a></b>\n
<b>👲 Developer : <a href='https://telegram.me/tellybots_4u'>TellyBots_4u</a></b>\n
<b>📦 Last Updated : <a href='https://telegram.me/tellybots_4u'>[ 18-Oct-21 ] 3:00 PM</a></b>\n
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [
                    [InlineKeyboardButton('📡 Update Channel', url='https://t.me/tellybots_4u'), InlineKeyboardButton('💬 Support Group', url='https://t.me/tellybots_support')],
                    [InlineKeyboardButton('🚦 Bot Status', url='https://t.me/tellybots_4u'), InlineKeyboardButton('⛔ Close', callback_data='close')]
                ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    DOWNLOAD_START = "<b>Downloading to my server now 📥</b> \n\n<code>Please wait Uploading will Start as soon as possible 🤹...</code>"
    UPLOAD_START = "Uploading to Telegram now 📤..."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS =  "Downloaded in <b>{}</b> seconds.\n\nUploaded in <b>{}</b> seconds.\n\n<b>Thanks For Using Me</b>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom Thumbnail Saved. This Image Will Be Used in Your Next Upload 📁.\n\nIf you want to delete it send\n /deletethumbnail anytime!"
    DEL_ETED_CUSTOM_THUMB_NAIL = "Custom Thumbnail Cleared Successfully 🌀.\nYou will now get an auto generated thumbnail for your video uploads!"
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""

    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thanks for using @xurluploaderbot)"
    
    
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    

    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /genthumbnail to a media album, to generate custom thumbnail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
