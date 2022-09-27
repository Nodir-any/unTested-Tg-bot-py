# pip install python-telegram-bot
from telegram.ext import *

import keys

print('Starting up bot...')


# use the /start command
def start_command(update, context):
    update.message.reply_text('Hello there! I\'m searchIt bot. How can I help?')


# use the /help command
def help_command(update, context):
    update.message.reply_text('If you are having issues, pls leave your contact information, we will reach out to you ASAP!')


# use the /some other command
def custom_command(update, context):
    update.message.reply_text('This is your personal command, you can add whatever text you want here.')


def handle_response(text) -> str:
    

    if 'hello' or 'hi' in text:
        return 'Hey there!'

    if ' ' in text:
        return 'I am a searchIt bot and you can search whatever you like here, I will help you find it!'

    return 'I don\'t understand'


def handle_message(update, context):
    # info of the incoming message
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    # bot reacts to group message if mentioned
    if message_type == 'group':
        # put your bot username
        if '@random' in text:
            new_text = text.replace('@random', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    # Reply normal if the message is in private
    update.message.reply_text(response)


# Log errors
def error(update, context):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
