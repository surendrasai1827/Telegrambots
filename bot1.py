from telegram.ext import Application, MessageHandler, filters

BOT1_TOKEN = "8434050747:AAG7vGcZVanylxrJ2bR7lyxJ6GLqgfI4scM"
GROUP_A = -1003613099017
GROUP_B = -1003624477633

TAG = "[BOT1]"

async def forward(update, context):
    msg = update.message
    if not msg:
        return

    text = msg.text or msg.caption or ""
    if TAG in text:
        return

    if msg.chat_id == GROUP_A:
        await msg.copy(chat_id=GROUP_B, caption=text + " " + TAG)
    elif msg.chat_id == GROUP_B:
        await msg.copy(chat_id=GROUP_A, caption=text + " " + TAG)

app = Application.builder().token(BOT1_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))
app.run_polling()