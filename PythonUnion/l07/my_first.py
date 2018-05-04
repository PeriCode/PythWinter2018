import telebot

TOKEN = '466722732:AAE_Qa6IVzyPgZhc57lWSQ1KP53JQPpej5w'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def answer(message):
	bot.send_message(message.chat.id, 'Ура! Я побрился!')

@bot.message_handler(regexp = 'спойлер')
def hate(message):
	bot.send_message(message.chat.id, 'DC - лучше')

@bot.message_handler(func = lambda message:True)
def kek(message):
	if message.text == 'Как фильм?':
		bot.send_message(message.chat.id, 'Гамора умрет!')
	elif message.text == 'Хватит спойлерить!!!':
		bot.send_message(message.chat.id, 'И паук тоже!')
	elif message.text == 'DC или Марвел?':
		bot.send_message(message.chat.id, 'Канешна Марвел!')

if __name__ == '__main__':
	bot.polling()