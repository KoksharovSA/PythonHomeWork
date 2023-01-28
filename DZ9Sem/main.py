from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

from SECRET import TELEGRAM_BOT_TOKEN
from bot_commands import *


print('Bot started')
app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

#app.add_handler(CallbackQueryHandler(button))
app.add_handler(CommandHandler("output", output))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("show", show))
app.add_handler(CommandHandler("show_all", show_all))
app.add_handler(CommandHandler("t", t))
app.add_handler(CommandHandler("s", s))
app.add_handler(CommandHandler("m", m))
app.add_handler(CommandHandler("st", st))
app.add_handler(MessageHandler(filters=filters.TEXT, callback=echo))

app.run_polling()