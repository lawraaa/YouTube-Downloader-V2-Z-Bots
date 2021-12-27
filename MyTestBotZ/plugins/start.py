from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⛄Cʜᴀɴɴᴇʟ", url="https://t.me/Z_Bots"), InlineKeyboardButton("⛄Cʀᴇᴀᴛᴏʀ", url="https://github.com/madtoazenzio") ],
        [InlineKeyboardButton(
            "⛄ Jᴏɪɴ ɴᴏᴡ ⛄", url="https://t.me/Z_Bots")]
    ])
    thumbnail_url = config.SPIC
    welcomed = f"""Hᴇʏ <b>{message.from_user.first_name}</b>\n\nA Sɪᴍᴘʟᴇ Yᴏᴜᴛᴜʙᴇ Dᴏᴡɴʟᴏᴀᴅᴇʀ Bᴏᴛ Tʜᴀᴛ Cᴀɴ:
  ➠ Dᴏᴡɴʟᴏᴀᴅ Yᴏᴜᴛᴜʙᴇ Vɪᴅᴇᴏs
  ➠ Dᴏᴡɴʟᴏᴀᴅ Aᴜᴅɪᴏ Fʀᴏᴍ Yᴏᴜᴛᴜʙᴇ Vɪᴅᴇᴏs \n\n Mᴀᴅᴇ Wɪᴛʜ ♥️ Bʏ @ᴢ_ʙᴏᴛs"""
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
