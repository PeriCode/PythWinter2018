import telebot

TOKEN = '466722732:AAE_Qa6IVzyPgZhc57lWSQ1KP53JQPpej5w'

bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
keyboard.row('Забанить Курбана', 'Разбанить Курбана')

@bot.message_handler(commands = ['banForKurban'])
def ban(message):
	msg = bot.send_message(message.chat.id, 'Голосуем, товарищи',
		reply_markup = keyboard)
	bot.register_next_step_handler(msg, ban_handler)

def ban_handler(message):
	if message.text == 'Забанить Курбана':
		bot.send_message(message.chat.id, 'Прощай, Курбан, скучать не будем!')
	elif message.text == 'Разбанить Курбана':
		bot.send_message(message.chat.id, 'Хабар принес?')

@bot.message_handler(commands = ['getRandomFilm'])
def get_film(message):
	line_kb = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру
	but_film = telebot.types.InlineKeyboardButton(text = 'Дай мне фильм, срочно!',
		callback_data = 'фильм') # создаем кнопку
	line_kb.add(but_film) # вешаем кнопку на клавиатуру

	but_kinopoisk = telebot.types.InlineKeyboardButton(text = 'Открыть кинопоиск',
		url = 'https://www.kinopoisk.ru') 
	line_kb.add(but_kinopoisk)
	but_serial = telebot.types.InlineKeyboardButton(text = 'Дай мне сериал, срочно!',
		callback_data = 'сериал')
	line_kb.add(but_serial)
	bot.send_message(message.chat.id, 'Что будем смотреть?', reply_markup = line_kb)

@bot.callback_query_handler(func = lambda call:True)
def random_film(callobj):
	if callobj.data == 'фильм':
		bot.send_message(callobj.message.chat.id, 'Властелин колец')
	elif callobj.data == 'сериал':
		bot.send_message(callobj.message.chat.id, 'Солдаты. Новый призыв.')

if __name__ == '__main__':
	bot.polling()