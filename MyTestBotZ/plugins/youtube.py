from datetime import datetime, timedelta
from pyrogram import Client, Filters, InlineKeyboardMarkup, InlineKeyboardButton
from MyTestBotZ import user_time
from config import youtube_next_fetch
from MyTestBotZ.helper.ytdlfunc import extractYt, create_buttons
import wget
import os
from PIL import Image
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1248974748 1401477467").split())

    
ytregex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"

@Client.on_message(Filters.regex(ytregex))
async def ytdl(bot, message):
    if message.from_user.id not in AUTH_USERS:
        return
    userLastDownloadTime = user_time.get(message.chat.id)
    try:
        if userLastDownloadTime > datetime.now():
            wait_time = round((userLastDownloadTime - datetime.now()).total_seconds() / 60, 2)
            await message.reply_text(f"`Wait {wait_time} Minutes before next Request`")
            return
    except:
        pass

    url = message.text.strip()
    await message.reply_chat_action("typing")
    try:
        title, thumbnail_url, formats = extractYt(url)

        now = datetime.now()
        user_time[message.chat.id] = now + \
                                     timedelta(minutes=youtube_next_fetch)

    except Exception:
        await message.reply_text("`ꜰᴀɪʟᴇᴅ ᴛᴏ ꜰᴇᴛᴄʜ ʏᴏᴜᴛᴜʙᴇ ᴅᴀᴛᴀ... 😔 \nᴘᴏssɪʙʟᴇ ʏᴏᴜᴛᴜʙᴇ ʙʟᴏᴄᴋᴇᴅ sᴇʀᴠᴇʀ ɪᴘ \n#error`")
        return
    buttons = InlineKeyboardMarkup(list(create_buttons(formats)))
    sentm = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ ʏᴏᴜᴛᴜʙᴇ ᴜʀʟ 🔎 🔎 🔎")
    try:
        # Todo add webp image support in thumbnail by default not supported by pyrogram
        # https://www.youtube.com/watch?v=lTTajzrSkCw
        img = wget.download(thumbnail_url)
        im = Image.open(img).convert("RGB")
        output_directory = os.path.join(os.getcwd(), "downloads", str(message.chat.id))
        if not os.path.isdir(output_directory):
            os.makedirs(output_directory)
        thumb_image_path = f"{output_directory}.jpg"
        im.save(thumb_image_path,"jpeg")
        await message.reply_photo(thumb_image_path, caption=title, reply_markup=buttons)
        await sentm.delete()
    except Exception as e:
        print(e)
        try:
            thumbnail_url = "https://telegra.ph/file/ce37f8203e1903feed544.png"
            await message.reply_photo(thumbnail_url, caption=title, reply_markup=buttons)
        except Exception as e:
            await sentm.edit(
            f"<code>{e}</code> #Error")

