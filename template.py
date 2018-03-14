# -*- coding: utf-8 -*-

import telebot
import sqlite3
import random

from telebot import types
print ('[+] Старт программы')

def menu_main ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное меню')
    return markup

def menu_dostavka ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Доставлен')
    return markup

def menu_curery ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Курьер01')
    markup.row('Курьер02')
    return markup


def menu_select_zakaz ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Заказ мой')
    markup.row('Плохой заказ')
    return markup



def load_staus (user_id):
    conn = sqlite3.connect("user.sqlite") 
    cursor = conn.cursor()
    sql = "select id,user_id,status from user where 1=1"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id,user_id,status = row
        print ('[+]',user_id,status)
    return status

def save_status (user_id,username,status):
    label = 'no'
    conn = sqlite3.connect("user.sqlite") 
    cursor = conn.cursor()
    sql = "select id,user_id from user where 1=1"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id,user_id = row
        print ('[+]',user_id)
        label = 'yes'
    if label == 'no':
        print ('[+] Новый User'+str(user_id))
        cursor = conn.cursor()
        a = [str(user_id),str(username),'','','','','','','','','',status]    
        cursor.execute("INSERT INTO user (user_id,username,name,first_name,last_name,setting01,setting02,setting03,setting04,setting05,setting06,status)VALUES (?,?,?,?,?,?,?,?,?,?,?,?);",a)    
        conn.commit()
    else:
        sql = "UPDATE user SET status = '"+str(status)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
        print ('[+] User изменен: '+str(user_id))
   
def save_param (user_id,nom,znak):
    conn = sqlite3.connect("user.sqlite") 
    cursor = conn.cursor()
    sql = "UPDATE user SET setting01 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
    cursor.execute(sql)
    conn.commit()
    sql = "UPDATE user SET setting02 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
    cursor.execute(sql)
    conn.commit()
    sql = "UPDATE user SET setting03 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
    cursor.execute(sql)
    conn.commit()
    sql = "UPDATE user SET setting04 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
    cursor.execute(sql)
    conn.commit()
    sql = "UPDATE user SET setting05 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
    cursor.execute(sql)
    conn.commit()

def load_param (user_id,nom):
    conn = sqlite3.connect("user.sqlite") 
    cursor = conn.cursor()
    sql = "select id,user_id,setting01 from user where 1=1"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id,user_id,setting01 = row
        print ('[+]',user_id,setting01)
    return setting01


def menu_agreg ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('UBER')
    markup.row('GETT')
    markup.row('Яндекс такси')
    return markup

def menu_main ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Яндекс такси')
    return markup



if __name__ == "__main__":
    print ('@SecretKanal_bot')
    token = '484307717:AAHiXSSTcltwzK-RWcK6mS-fheh9qM-ZXEQ'
    bot    = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    username   = message.from_user.username
    first_name = message.from_user.first_name
    last_name  = message.from_user.last_name
    user_id    = message.from_user.id
    date       = message.date
    message    = message.text
    print ('[+]',message,user_id)
    save_status (user_id,username,'start')
    save_param (user_id,1,'')
    save_param (user_id,2,'')
    save_param (user_id,3,'')
    save_param (user_id,4,'')
    save_param (user_id,5,'')
    save_param (user_id,6,'')

    message_out = 'Вас приветствует компания <b>РиалТакси!</b>\nОтветьте, пожалуйста, на вопросы:'
    bot.send_message(user_id,message_out,parse_mode='HTML')  

    message_out = 'Ваше ФИО?'    
    bot.send_message(user_id,message_out,parse_mode='HTML')    
    save_status (user_id,username,'FIO')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    user_id    = message.from_user.id 
    message    = message.text
    first_name = ''
    last_name  = ''
    username   = ''
    date       = ''
    print ('[+]',message)
    status = load_staus (user_id)
    print ('[+]',status)




    if message.find ('меню') != -1:
        markup = menu_select_zakaz ()
        message_out = 'Главное меню'
        markup = menu_main
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)     

    if status == 'FIO': 
        message_out = 'Спасибо'
        bot.send_message(user_id,message_out,parse_mode='HTML')
        save_param (user_id,1,message)
        save_status (user_id,username,'marka')
        message_out = 'Марка и год выпуска вашего автомобиля?'
        bot.send_message(user_id,message_out,parse_mode='HTML')
    
    if status == 'marka': 
        message_out = 'Спасибо'
        bot.send_message(user_id,message_out,parse_mode='HTML')
        save_param (user_id,2,message)
        save_status (user_id,username,'agreg')
        message_out = 'Марка и год выпуска вашего автомобиля?'
        bot.send_message(user_id,message_out,parse_mode='HTML')

    if status == 'agreg': 
        message_out = 'Спасибо'
        bot.send_message(user_id,message_out,parse_mode='HTML')
        save_param (user_id,3,message)
        save_status (user_id,username,'city')
        message_out = 'Если вы уже являетесь действующим водителем такси, то укажите в каких агрегаторах:\nUBER, GETT или Яндекс такси?'
        markup = menu_agreg ()
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)

    if status == 'city': 
        message_out = 'Спасибо'
        bot.send_message(user_id,message_out,parse_mode='HTML')
        save_param (user_id,4,message)
        save_status (user_id,username,'connect')
        message_out = 'В каком городе вы будете работать?'
        bot.send_message(user_id,message_out,parse_mode='HTML')

    if status == 'connect': 
        message_out = 'Спасибо'
        bot.send_message(user_id,message_out,parse_mode='HTML')
        save_param (user_id,5,message)
        save_status (user_id,username,'')
        markup = menu_agreg ()
        message_out = 'Kакую компанию хотите подключиться черезw нас:\nUBER, GETT или Яндекс такси?'
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)


        markup = menu_agreg ()
        

        setting01 = load_param (user_id,1)
        setting02 = load_param (user_id,2)
        setting03 = load_param (user_id,3)
        setting04 = load_param (user_id,4)
        setting05 = load_param (user_id,5)

        message_out = 'Ваши ответы:\n\n'+setting01+'\n'+setting02+'\n'+setting03+'\n'+setting04+'\n'+setting05+'\n'

        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)






        ###,reply_markup=markup

bot.polling()















