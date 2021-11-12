from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/Z_Bots"), InlineKeyboardButton("Creator", url="https://github.com/madtoazenzio") ],
        [InlineKeyboardButton(
            "⚡ Join Now ⚡", url="https://t.me/Z_Bots")]
    ])
    welcomed = f"""Hey <b>{message.from_user.first_name}</b>\nA Simple YouTube Downloader Bot that can:
  ➠ Download YouTube videos
  ➠ Download audio from YouTube videos \n\n Made with ♥️ by @Z_Bots"""
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
