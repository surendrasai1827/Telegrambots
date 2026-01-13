from telegram.ext import Application, MessageHandler, filters

BOT1_TOKEN = "8434050747:AAGyny5RBwXZp6KM53vQO2CTzzBO0LvhU4Y"

GROUP_A = -1003613099017   # Group A
GROUP_B = -1003624477633   # Group B

async def forward(update, context):
    msg = update.message
    if not msg:
        return

    # Ignore messages sent by THIS bot itself
    if msg.from_user and msg.from_user.username == context.bot.username:
        return

    text = msg.text or msg.caption or ""

    if msg.chat_id == GROUP_A:
        await msg.copy(chat_id=GROUP_B, caption=text)

    elif msg.chat_id == GROUP_B:
        await msg.copy(chat_id=GROUP_A, caption=text)

app = Application.builder().token(BOT1_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))
app.run_polling()