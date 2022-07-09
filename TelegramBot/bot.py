import telebot
from telebot import types

TOKEN = "5475633161:AAHJs4Y3Abac-BJb6GMj5ZR6-4mvZLI4bvM"

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello!! How may I help you?")

@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)

bot.infinity_polling()