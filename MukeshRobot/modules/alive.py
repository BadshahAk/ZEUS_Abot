import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from MukeshRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID

PHOTO = [
    "https://telegra.ph/file/245e2812e8ff07391fd10.jpg",
    "https://telegra.ph/file/1226413ee51834139b310.jpg",
    "https://telegra.ph/file/83fa16123e7c5ae2df9e9.jpg",
    "https://telegra.ph/file/97c64f62041be0dd0b654.jpg",
    "https://telegra.ph/file/0417d3c1726da3c1f7c45.jpg",
]

Mukesh = [
    [
        InlineKeyboardButton(text="𝙇𝙀𝙂𝙀𝙉𝘿", url=f"https://t.me/Brahman_Anand"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="➕ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

lol = "https://telegra.ph/file/ea140783bd9854833c461.jpg"


@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.1)
    await accha.edit("𝐖𝐚𝐢𝐭𝐢𝐧𝐠..")
    await asyncio.sleep(0.1)
    await accha.edit("𝐖𝐚𝐢𝐭𝐢𝐧𝐠...")
    await accha.delete()
    await asyncio.sleep(0.1)
    umm = await m.reply_sticker(
        "CAADBQADcgkAAoCLSFV4lcD251tTkwI"
    )
    await umm.delete()
    await asyncio.sleep(2)
    await m.reply_photo(
        lol,
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ 『[ZΞUS](f"t.me/{BOT_USERNAME}")』**
   ┏━━━━━━━━━━━━━━━━━❥
   ┣ ᴏᴡɴᴇʀ​ 👉 [𓆩𝙇𝙀𝙂𝙀𝙉𝘿 ♡ 𝘼𝙉𝘼𝙉𝘿𓆪](https://t.me/Brahman_Anand)
   ┣ 𝙲𝚑𝚊𝚝 👉 [⤹ 𝑪𝑯𝑨𝑻𝑻𝑰𝑵𝑮𝒙𝑮𝑹𝑶𝑼𝑷 ⤸](https://t.me/CHATTINGxGROUP)
   ┗━━━━━━━━━━━━━━━━━❥""",
        reply_markup=InlineKeyboardMarkup(Mukesh),
    )
__mod_name__ = "⍟ ᴀʟɪᴠᴇ ⍟"
__help__ = """
 ©️ [ᴍᴜᴋᴇsʜ] (f"tg://user?id={OWNER_ID}"))

*ᴜsᴇʀ ᴄᴏᴍᴍᴀɴᴅs*:
» /alive*:* ᴛᴏ ᴄʜᴇᴀᴋ ❓  ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ?"""
