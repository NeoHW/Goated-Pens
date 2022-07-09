import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "5475633161:AAHJs4Y3Abac-BJb6GMj5ZR6-4mvZLI4bvM"

bot = telebot.TeleBot(TOKEN, parse_mode=None)
started = False

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Elderly", callback_data="cb_elderly"),
                               InlineKeyboardButton("Kids", callback_data="cb_kids"))
    return markup

def choosing_org():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("MWS- Nursing Home", callback_data="cb_elderly"),
                               InlineKeyboardButton("", callback_data="cb_kids"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_elderly":
        bot.send_message(call.message.chat.id, "Elderly! Which organisation do you want to assist?", reply_markup=gen_markup())
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "cb_kids":
        bot.answer_callback_query(call.id, "Answer is No")

start_message = "What beneficiary do you want to service"
@bot.message_handler(commands=['start'])
def message_handler(message):
    bot.send_message(message.chat.id, start_message, reply_markup=gen_markup())
    

bot.polling()