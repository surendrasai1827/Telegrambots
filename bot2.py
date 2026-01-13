from telegram.ext import Application, MessageHandler, filters

BOT2_TOKEN = "YOUR_BOT2_TOKEN"
GROUP_B = -100BBBBBBBBBB
GROUP_C = -100CCCCCCCCCC

async def forward(update, context):
    msg = update.message
    if not msg:
        return

    # C → B (ANY sender)
    if msg.chat_id == GROUP_C:
        await msg.copy(chat_id=GROUP_B)

    # B → C (ONLY if not sent by THIS bot)
    elif msg.chat_id == GROUP_B:
        if msg.from_user and msg.from_user.username == context.bot.username:
            return
        await msg.copy(chat_id=GROUP_C)

app = Application.builder().token(BOT2_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))
app.run_polling()