from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

import tic_tac_toe as xo


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    xo.cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    keyboard = [["11", "12", "13"],
                ["21", "22", "23"],
                ["31", "32", "33"],
                ["/start"]]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    await update.message.reply_text(f'{xo.field()}')
    await update.message.reply_text('Сделайте ход', reply_markup=reply_markup)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = xo.ttt(update.message.text)
    await update.message.reply_text(f'{xo.field()}')
    await update.message.reply_text(f'{message}')
    