from telegram.ext import Application, MessageHandler, filters

BOT2_TOKEN = "8164514482:AAF8-pgWnIG7HoYh4dWx2wM9rMxctmrn6Q8"
GROUP_B = -1003624477633
GROUP_C = -1003551352561

TAG = "[BOT2]"

async def forward(update, context):
    msg = update.message
    if not msg:
        return

    text = msg.text or msg.caption or ""
    if TAG in text:
        return

    if msg.chat_id == GROUP_B:
        await msg.copy(chat_id=GROUP_C, caption=text + " " + TAG)
    elif msg.chat_id == GROUP_C:
        await msg.copy(chat_id=GROUP_B, caption=text + " " + TAG)

app = Application.builder().token(BOT2_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))
app.run_polling()