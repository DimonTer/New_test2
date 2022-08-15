from config import token
import telebot


bot = telebot.TeleBot(token)

@bot.message_handler()
def func(message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()
