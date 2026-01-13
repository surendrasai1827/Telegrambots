from telegram.ext import Application, MessageHandler, filters

BOT1_TOKEN = "8434050747:AAGyny5RBwXZp6KM53vQO2CTzzBO0LvhU4Y"
GROUP_A = -1003613099017
GROUP_B = -1003624477633

TAG = "[BOT1]"

async def forward(update, context):
    msg = update.message
    if not msg or not msg.text:
        return

    # Prevent loop
    if TAG in msg.text:
        return

    if msg.chat_id == GROUP_A:
        await msg.copy(chat_id=GROUP_B, caption=(msg.text + " " + TAG))
    elif msg.chat_id == GROUP_B:
        await msg.copy(chat_id=GROUP_A, caption=(msg.text + " " + TAG))

app = Application.builder().token(BOT1_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))
app.run_polling()
