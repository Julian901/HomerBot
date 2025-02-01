import telebot

token = '7631840452:AAH4O93qQ6J914x5FhPTQX7YhJC3bTiJ_XA' #Вставьте Ваш токен, полученный от BotFather
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start']) #Для команды /start, можете изменить на любую другую
def start_join(message):
    bot.send_message(message.chat.id, text="Запустите приложение, нажав на кнопку ниже.")

bot.polling(none_stop=True) #Чтобы бот работал бесперебойно, пока запущена программа