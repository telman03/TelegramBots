import telebot

bot = telebot.TeleBot('5168616201:AAGzeu20-tddkgUEhnItL5YpmRFLacBPWkE')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Say something to repeat it back!')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'What you wrote: ' + message.text)

bot.polling(none_stop=True, interval=0)