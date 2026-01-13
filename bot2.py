from telegram.ext import Application, MessageHandler, filters

BOT2_TOKEN = "8164514482:AAG2Jtb2a7sMEGG LJ5Huk7Q-kRkRKz5dWww"

GROUP_B = -1003624477633   # Group B
GROUP_C = -1003551352561   # Group C

async def forward(update, context):
    msg = update.message
    if not msg:
        return

    # Ignore messages sent by THIS bot itself
    if msg.from_user and msg.from_user.username == context.bot.username:
        return

    text = msg.text or msg.caption or ""

    if msg.chat_id == GROUP_B:
        await msg.copy(chat_id=GROUP_C, caption=text)

    elif msg.chat_id == GROUP_C:
        await msg.copy(chat_id=GROUP_B, caption=text)

app = Application.builder().token(BOT2_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))
app.run_polling()