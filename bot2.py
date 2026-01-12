from telegram.ext import Application, MessageHandler, filters

BOT2_TOKEN = "PASTE_BOT2_TOKEN"
GROUP_B = -1002222222222
GROUP_C = -1003333333333

TAG = "[BOT2]"

async def forward(update, context):
    msg = update.message
    if not msg or not msg.text:
        return

    # Prevent loop
    if TAG in msg.text:
        return

    if msg.chat_id == GROUP_B:
        await msg.copy(chat_id=GROUP_C, caption=(msg.text + " " + TAG))
    elif msg.chat_id == GROUP_C:
        await msg.copy(chat_id=GROUP_B, caption=(msg.text + " " + TAG))

app = Application.builder().token(BOT2_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))
app.run_polling()
