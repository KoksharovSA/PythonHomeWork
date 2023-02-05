from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

from SECRET import TELEGRAM_BOT_TOKEN
from bot_commands import *


print('Bot started')
app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters=filters.TEXT, callback=echo))

app.run_polling()