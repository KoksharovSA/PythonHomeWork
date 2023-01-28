import csv
import datetime

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

list_metal = []
notes = []
current_thickness = ''
current_material = ''
current_size = ''
current_number = 0


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [["/start", "/output", "/add", "/show", "/show_all"],
                ["/t 0,8", "/t 1", "/t 1,2", "/t 2", "/t 3", "/t 4", "/t 5"],
                ["/t 6", "/t 8", "/t 10", "/t 12", "/t 14", "/t 16", "/t 20"],
                ["/s 1900\n1250", "/s 2500\n800", "/s 2500\n1250", "/s 2600\n1500", "/s 3000\n1500"],
                ["/m Нерж", "/m Оц", "/m гк", "/m 65г"]]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите материал', reply_markup=reply_markup)

async def t(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text.split()
    global current_thickness
    current_thickness = f'{message[1]}'
    await update.message.reply_text(f'Выбрана толщина S={current_thickness}')

async def s(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text.split()
    global current_size
    current_size = f'{message[1]}x{message[2]}'
    await update.message.reply_text(f'Выбран размер листа: {current_size}')
    
async def m(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text.split()
    global current_material
    current_material = f'{message[1]}'
    await update.message.reply_text(f'Выбран материал: {current_material}')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text.split()
    global current_number
    current_number += sum([int(x) for x in message if x.isdigit()])
    
async def st(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text.split()
    global current_number
    current_number -= sum([int(x) for x in message if x.isdigit()])
    
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global current_thickness
    global current_material
    global current_size
    global current_number
    if f'{current_material}{current_thickness}{current_size}' not in [f'{x[0]}{x[1]}{x[2]}' for x in list_metal]:
        list_metal.append([current_thickness, current_material, current_size, current_number])
        await update.message.reply_text(f'Добавлен металл: {current_thickness}{current_material}'
                                        f' {current_size} - {current_number} щт.')
        current_thickness = ''
        current_material = ''
        current_size = ''
        current_number = 0
    else:
        for index, item in enumerate(list_metal):
            if current_material == item[0] and current_thickness == item[1] and current_size == item[2]:
                list_metal[index] = [current_thickness, current_material, current_size, current_number+item[3]]
                await update.message.reply_text(f'Добавлен металл: {current_thickness}{current_material}'
                                                f' {current_size} - {current_number} щт.')
                current_thickness = ''
                current_material = ''
                current_size = ''
                current_number = 0
        
async def output(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    date = datetime.date.today().strftime("%d_%m_%y")
    text = f'output/base_metal_{date}.csv'
    with open(text, 'w', newline='', encoding='utf-8') as data:
        base_writer = csv.writer(data, delimiter=',')
        base_writer.writerows(list_metal)
    await update.message.reply_text(f'Создан файл: {text}')

async def show(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global current_thickness
    global current_material
    global current_size
    global current_number
    text = f'{current_thickness}{current_material} {current_size} - {current_number} шт.\n'
    await update.message.reply_text(text)

async def show_all(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ''
    for item in list_metal:
        text += f'{item[0]}{item[1]} {item[2]} - {item[3]} шт.\n'
    await update.message.reply_text(text)
