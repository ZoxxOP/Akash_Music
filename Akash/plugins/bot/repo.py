from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Akash import app

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ 𝐀ɴᴀɴʏᴀ 𝐁ᴏᴛs 𝐑ᴇᴘᴏs ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 𝗥ᴇᴘᴏ 𝗢ᴡɴᴇʀ ᴋᴏ 

✰ || @WTF_NoHope ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""

@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{app.username}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝐇ᴇʟᴘ", url="https://t.me/AnanyaBotSupport"),
          InlineKeyboardButton("𝐀ᴋᴀsʜ", url="https://t.me/WTF_NoHope"),
          ],
               [
                InlineKeyboardButton("𝐀ɴᴀɴʏᴀ 𝐁ᴏᴛs", url=f"https://t.me/AnanyaBots"),
],
[
InlineKeyboardButton("𝐌ᴀɪɴ 𝐁ᴏᴛ", url=f"https://t.me/Ananya_VcMusic_Bor"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/12p43f.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
