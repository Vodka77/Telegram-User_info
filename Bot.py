import telebot 
import requests
import random 
import vodka
from telebot import types
from time import sleep
import time
import os,sys
def vodka(s):
 for ASU in s + '\n':
  sys.stdout.write(ASU)
  sys.stdout.flush()
  sleep(2./600)
Z = '\x1b[1;31m'#احمر
X = '\x1b[1;32m'#اخضر
C = '\x1b[1;33m'#yellow
V = '\x1b[1;34m'#blue	
B = '\x1b[1;35m'#pink
N = '\x1b[1;36m'#لبني
M = '\x1b[1;37m'#ابيض	 
t = time.localtime()
current_time = time.strftime('%H:%M:%S', t)
current_date =  time.strftime('%D', t)
vodka(X+'__     _____  ____  _  __    _    ')
vodka(Z+'\ \   / / _ \|  _ \| |/ /   / \   ')
vodka(X+' \ \ / / | | | | | |   /   / _ \  ')
vodka(Z+'  \ V /| |_| | |_| | . \  / ___ \ ')
vodka(X+'   \_/  \___/|____/|_|\_\/_/   \_\ ')
vodka(N+'Time Now : '+M+current_time)
vodka(N+'Date Now : '+M+current_date)
vodka(M+'- - - - - - - - - - - - - - - - - - - - ')
vodka(Z+'('+X+'⌯'+Z+')'+N+'Telegram : '+M+'@Vodka_tk')
vodka(Z+'('+X+'⌯'+Z+')'+N+'GitHub : '+M+'https://github.com/Vodkahunter.com')
vodka(Z+'('+X+'⌯'+Z+')'+N+'Program Code : '+M+'python3')
vodka(Z+'('+X+'⌯'+Z+')'+N+'Program App : '+M+'pycharm')
vodka(M+'- - - - - - - - - - - - - - - - - - - - ')
Token = input(N+'('+B+'⌯'+N+')'+B+'Enter Token : '+M)
bot = telebot.TeleBot(Token)
co = types.InlineKeyboardButton(text ="- VODKA_Tools </>",url='https://t.me/Vodka_Tools')
by = types.InlineKeyboardButton(text ="- Version",callback_data = 'vodka')
@bot.message_handler(commands=['start'])
def first(message):
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co,by)    
    bot.send_message(message.chat.id , f'<b>Hi VODKA #1st - python☬\n- - - - - - - - - - - - - -\nWelcome To Telegram UserName Info!\nSend User Name With Out @ To Get Info\n- - - - - - - - - - - - - -\nBy  : @Vodka_tk</b>', parse_mode="html",reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "vodka":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="- VERSION 0.0.1")
@bot.message_handler(func=lambda m:True) 
def gg(message):
    msg = message.text
    url = requests.get(f'https://apis.red/api/tginfo/?user={msg}').json()  
    z = url['bio']   
    x = url['name'] 
    c = url['pic']
    v = url['subscribers']
    bot.send_message(message.chat.id,f'<b>Hi VODKA #1st - python☬ Your Result\n- - - - - - - - - - -\nBio : {z}\nName : {x}\nSubs : {v}\nUser Name : @{msg}\n- - - - - - - - - - -\nBY : @VODKA_Tk</b>',parse_mode='html')
pass
bot.polling(True)    
