import telebot as tb 
from telebot import types as tp
import config
import platforms_info as pinfo
import minifuncs as minif
import sqlite3 as sql3


bot = tb.TeleBot(config.TGRAM_KEY)

@bot.message_handler(commands=['menu'])
def payment(msg):
    
    
    bot.send_message( msg.id )
    
    


    

bot.infinity_polling()
