from telegram.ext import Application, MessageHandler, filters

BOT2_TOKEN = 8164514482:AAG2Jtb2a7sMEGGLJ5Huk7Q-kRkRKz5dWww
GROUP_B = -1003624477633
GROUP_C = -1003551352561

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
