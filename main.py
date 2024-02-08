from turtle import update
from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: final = '6371096310:AAGq9YvyPNlpXkc_NHb_bSVaWlIa1_7aXeI'
BOT_USERNAME: final = '@Fazril BOT'


# PERINTAH
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Halo! Terimakasih telah mencoba bot saya! Perkenalkan saya Fazril')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Saya Bot Fazril! Mohon ketik sesuatu supaya bot saya bisa merespon Anda!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Ini adalah perintah kustom')


# Respon
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'Halo' in processed:
        return 'Halo juga!'
    
    if 'Apa kabarmu' in processed:
        return 'Kabar saya baik!'
    
    if 'Apakah Anda Suka membuat program di Laptop' in processed:
        return 'Ya, saya sangat suka sekali'
    
    return 'Saya tidak mengerti apa yang anda ketik'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # PERINTAH
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    # PESAN
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # ERRORS
    app.add_error_handler(error)

    # polls the Bot
    print('Polling')
    app.run_polling(poll_interval=3)

