from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden

api_id = "28762542"
api_hash = "7ecef38bbe9e8a286372c5c50100423c"
bot_token = "7216566711:AAEPTM29DRDpm4tVHF1EjpjPgnav1vyPCUU"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

X = "USERNAEM"

@app.on_message(filters.incoming & filters.private, group=-1)
async def channel(app: Client, msg: Message):
    if not X:
        return
    try:
        try:
            await app.get_chat_member(X, msg.from_user.id)
        except UserNotParticipant:
            if X.isalpha():
                link = "https://t.me/TeamSamrat" + X
            else:
                chat_info = await app.get_chat(X)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/6ab1b2c09f0b0d81d7c52.jpg", caption=f"๏ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ʏᴏᴜ'ᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ [๏sᴜᴘᴘᴏʀᴛ๏]({link}) ʏᴇᴛ, ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛʜᴇɴ ᴊᴏɪɴ [๏sᴜᴘᴘᴏʀᴛ๏]({link}) ᴀɴᴅ sᴛᴀʀᴛ ᴍᴇ ᴀɢᴀɪɴ ! ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("๏Jᴏɪɴ๏", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_Jᴏɪɴ ᴄʜᴀᴛ ๏: {X} !")

app.run()

