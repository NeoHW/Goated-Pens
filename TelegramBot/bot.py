import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "5475633161:AAHJs4Y3Abac-BJb6GMj5ZR6-4mvZLI4bvM"

bot = telebot.TeleBot(TOKEN, parse_mode=None)
started = False

start_message = "What beneficiary do you want to service?"
@bot.message_handler(commands=['start'])

def message_handler(message):
    bot.send_message(message.chat.id, start_message, reply_markup=choosing_bene())

def choosing_bene():
    # markup is keyboard
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add( InlineKeyboardButton("Elderly", callback_data="cb_elderly"),
                InlineKeyboardButton("Kids", callback_data="cb_kids"),
                InlineKeyboardButton("Special Needs", callback_data="cb_sn"),
                InlineKeyboardButton("Pet", callback_data="cb_pet"))
    return markup

def choosing_eld_org():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add( InlineKeyboardButton("MWS- Nursing Home", callback_data="cb_mwsnh"),
                InlineKeyboardButton("MWS Bethany Nursing Home", callback_data="cb_bnh"),
                InlineKeyboardButton("Pacific Healthcare Nursing Home", callback_data="cb_phnh"))
    return markup

def choosing_sn_org():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add( InlineKeyboardButton("Movement for the Intellectually Disabled of Singapore", callback_data="cb_minds"),
                InlineKeyboardButton("Handicaps Welfare Association", callback_data="cb_hwa"),
                InlineKeyboardButton("Down Syndrome Association", callback_data="cb_dsa"))
    return markup

def choosing_pet_org():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add( InlineKeyboardButton("Action For Singapore Dogs", callback_data="cb_asd"),
                InlineKeyboardButton("Hope Dog Rescue", callback_data="cb_hdr"),
                InlineKeyboardButton("Love The Voiceless", callback_data="cb_ltv"))
    return markup

def choosing_kid_org():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add( InlineKeyboardButton("Singapore Children's Society", callback_data="cb_scs"),
                InlineKeyboardButton("Club Rainbow", callback_data="cb_cr"),
                InlineKeyboardButton("Make A Wish Foundation", callback_data="cb_mawf"))
    return markup

@bot.callback_query_handler(func=None)
def callback_query(call):
    if call.data == "cb_elderly":
        bot.send_message(call.message.chat.id, "Elderly! Which organisation do you want to assist?", reply_markup=choosing_eld_org())
        bot.answer_callback_query(call.id, "Thank you for assisting our elderly")
    elif call.data == "cb_kids":
        bot.send_message(call.message.chat.id, "Kids! Which organisation do you want to assist?", reply_markup=choosing_kid_org())
        bot.answer_callback_query(call.id, "Thank you for assisting our children")
    elif call.data == "cb_sn":
        bot.send_message(call.message.chat.id, "Special needs! Which organisation do you want to assist?", reply_markup=choosing_sn_org())
        bot.answer_callback_query(call.id, "Thank you for assisting our special needs population")   
    elif call.data == "cb_pet":
        bot.send_message(call.message.chat.id, "Pets! Which organisation do you want to assist?", reply_markup=choosing_pet_org())
        bot.answer_callback_query(call.id, "Thank you for assisting our animals") 

    
def main():   
    bot.polling()

if __name__ == "__main__":
    main()