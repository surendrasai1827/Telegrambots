from telegram.ext import Application, MessageHandler, filters

BOT1_TOKEN = "8434050747: AAGyny5RBwXZp6K M53vQ02CTzzB00LvhU4Y"
GROUP_A = -1003613099017
GROUP_B = -1003624477633

async def forward(update, context):
    msg = update.message
    if not msg:
        return

    # A → B (ANY sender: human or bot)
    if msg.chat_id == GROUP_A:
        await msg.copy(chat_id=GROUP_B)

    # B → A (ONLY if message came from Bot2 or human)
    elif msg.chat_id == GROUP_B:
        # Prevent infinite loop: ignore messages sent by THIS bot
        if msg.from_user and msg.from_user.username == context.bot.username:
            return
        await msg.copy(chat_id=GROUP_A)

app = Application.builder().token(BOT1_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))
app.run_polling()