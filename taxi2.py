# -*- coding: utf-8 -*-

import telebot
import sqlite3
import random

from telebot import types
print ('[+] Старт программы')

def menu_main ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное меню')
    markup.row('Админка','Добавить <?>')
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
    sql = "select id,user_id,status from user where user_id = '"+str(user_id)+"'"
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
    sql = "select id,user_id from user where user_id = '"+str(user_id)+"'"
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
    if nom == 1:
        sql = "UPDATE user SET setting01 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 2:
        sql = "UPDATE user SET setting02 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 3:        
        sql = "UPDATE user SET setting03 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 4:        
        sql = "UPDATE user SET setting04 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 5:        
        sql = "UPDATE user SET setting05 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 6:        
        sql = "UPDATE user SET setting06 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()

def load_param (user_id,nom):
    conn = sqlite3.connect("user.sqlite") 
    cursor = conn.cursor()
    sql = "select id,user_id,setting01,setting02,setting03,setting04,setting05,setting06 from user where user_id = '"+str(user_id)+"'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id,user_id,setting01,setting02,setting03,setting04,setting05,setting06 = row
        if nom == 1:
            print ('[+1]',user_id,setting01)
            return setting01
        if nom == 2:
            print ('[+2]',user_id,setting02)
            return setting02
        if nom == 3:
            print ('[+3]',user_id,setting03)
            return setting03
        if nom == 4:
            print ('[+4]',user_id,setting04)
            return setting04
        if nom == 5:
            print ('[+5]',user_id,setting05)
            return setting05
        if nom == 6:
            print ('[+6]',user_id,setting06)
            return setting06


def menu_agreg ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('UBER')
    markup.row('GETT')
    markup.row('Яндекс такси')
    return markup
    
    
def endfinish (user_id):
    if 1==1:
        if 1==1:    
            setting01 = load_param (user_id,1)
            setting02 = load_param (user_id,2)
            setting03 = load_param (user_id,3)
            setting04 = load_param (user_id,4)
            setting05 = load_param (user_id,5)
            message_out = 'Ваша заявка на подключение к такси передана специалисту. В связи с большим количеством обращений, специалист подключения свяжется с Вами в течение 2-3 часов.\n<b>Ваши ответы:</b>\n\n'+setting01+'\n'+setting02+'\n'+setting03+'\n'+setting04+'\n'+setting05+'\n'
            markup = menu_main ()
            bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
            ###,reply_markup=markup
            
            if 1==1:
            
                if setting02.find ('photos') != -1:            
                    message_out = 'фото на 2 вопрос'
                    bot.send_message(user_id,message_out,parse_mode='HTML')
                    img = open('/root/Language/'+setting02+'', 'rb')
                    bot.send_photo(user_id, img)                

                if setting03.find ('photos') != -1:            
                    message_out = 'фото на 3 вопрос'
                    bot.send_message(user_id,message_out,parse_mode='HTML')
                    img = open('/root/Language/'+setting03+'', 'rb')
                    bot.send_photo(user_id, img)                

                if setting04.find ('photos') != -1:            
                    message_out = 'фото на 4 вопрос'
                    bot.send_message(user_id,message_out,parse_mode='HTML')
                    img = open('/root/Language/'+setting04+'', 'rb')
                    bot.send_photo(user_id, img)                

                if setting05.find ('photos') != -1:            
                    message_out = 'фото на 5 вопрос'
                    bot.send_message(user_id,message_out,parse_mode='HTML')
                    img = open('/root/Language/'+setting05+'', 'rb')
                    bot.send_photo(user_id, img)                

            
            
    
    

if __name__ == "__main__":
    print ('@RUMTAXIMENBOT')
    token = '484307717:AAHiXSSTcltwzK-RWcK6mS-fheh9qM-ZXEQ'
    token = '512898072:AAEVJHmAx6hn-EkzMijkJZUDo5kK4ZW5_ac'
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
    ##save_param (user_id,1,'')
    ##save_param (user_id,2,'')
    ##save_param (user_id,3,'')
    ##save_param (user_id,4,'')
    ##save_param (user_id,5,'')
    #3save_param (user_id,6,'')
    message_out = 'Добрый День Вас приветствует компания RUMTAXI!\nНаш бот поможет вам подключиться к агрегаторам такси удаленно!\nПожалуйста введите свой номер телефона. и ответьте на вопросы бота:'
    markup =  menu_main ()
    bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)  
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
    
    Labeladmin = 'Good'

    if message.find ('Главное меню') != -1:
        markup = menu_select_zakaz ()
        message_out = 'Ваше ФИО?'    
        bot.send_message(user_id,message_out,parse_mode='HTML')    
        save_status (user_id,username,'FIO')
        Labeladmin = 'admin' 

    if message.find ('Добавить <?>') != -1:
        markup = menu_select_zakaz ()
        message_out = 'Напишите вопрос'
        markup = menu_main ()
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
        Labeladmin = 'admin' 
        save_status (user_id,username,'qwest')


    if message.find ('Админка') != -1:
    
        if str(user_id) == '260637021':    
            markup = menu_select_zakaz ()
            message_out = 'Главное меню'
            markup = menu_main ()        
            conn = sqlite3.connect("user.sqlite") 
            cursor = conn.cursor()
            sql = "select id,user_id,username,name,first_name,last_name,setting01,setting02,setting03,setting04,setting05,setting06 from user where 1=1"        
            message_out = 'Админка'
            bot.send_message(user_id,message_out,parse_mode='HTML')        
            cursor.execute(sql)
            data = cursor.fetchall()
            for row in data:
                id_v,user_id_v,username_v,name_v,first_name_v,last_name_v,setting01,setting02,setting03,setting04,setting05,setting06 = row   
                message_out = '<b>id user: '+str(user_id_v)+'</b>\n'+'username: '+str(username_v)+'\n'+'first_name: '+str(first_name_v)+'\n'
                message_out = message_out +'last_name: '+str(last_name)+'\n'+'setting01: '+str(setting01)+'\n'+'setting02: '+str(setting02)+'\n'+'setting03: '+str(setting03)+'\n'
                message_out = message_out + 'setting03: '+str(setting03)+'\n'+'setting04: '+str(setting04)+'\n'+'setting05: '+str(setting05)+'\n'+'setting06: '+str(setting06)
                bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
                Labeladmin = 'admin'

                if setting02.find ('photos') != -1:            
                    message_out = 'фото на 2 вопрос'
                    bot.send_message(user_id,message_out,parse_mode='HTML')
                    img = open('/root/Language/'+setting02+'', 'rb')
                    bot.send_photo(user_id, img)                

                if setting03.find ('photos') != -1:            
                    message_out = 'фото на 3 вопрос'
                    bot.send_message(user_id,message_out,parse_mode='HTML')
                    img = open('/root/Language/'+setting03+'', 'rb')
                    bot.send_photo(user_id, img)                

                if setting04.find ('photos') != -1:            
                    message_out = 'фото на 4 вопрос'
                    bot.send_message(user_id,message_out,parse_mode='HTML')
                    img = open('/root/Language/'+setting04+'', 'rb')
                    bot.send_photo(user_id, img)                

                if setting05.find ('photos') != -1:            
                    message_out = 'фото на 5 вопрос'
                    bot.send_message(user_id,message_out,parse_mode='HTML')
                    img = open('/root/Language/'+setting05+'', 'rb')
                    bot.send_photo(user_id, img)                

                if setting06.find ('photos') != -1:            
                    message_out = 'фото на 6 вопрос'
                    bot.send_message(user_id,message_out,parse_mode='HTML')
                    img = open('/root/Language/'+setting06+'', 'rb')
                    bot.send_photo(user_id, img)   
        else:
            message_out = 'Ваш код '+str(user_id)+' Вы не администратор.'
            bot.send_message(user_id,message_out,parse_mode='HTML')        

        
        
                                         

                

                
            Labeladmin = 'admin'

            
                           

    if Labeladmin == 'Good':
        if message.find ('меню') != -1:
            markup = menu_select_zakaz ()
            message_out = 'Главное меню'
            markup = menu_main ()
            bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
            
        if status == 'qwest': 
            message_out = 'Спасибо'
            bot.send_message(user_id,message_out,parse_mode='HTML')
            message_out = 'Вопрос записан\n\n<b>Список вопросов</b>'
            bot.send_message(user_id,message_out,parse_mode='HTML')
            conn = sqlite3.connect("qwest.sqlite") 
            cursor = conn.cursor()
            a = [message]    
            cursor.execute("INSERT INTO table2 (qw) VALUES (?);",a)    
            conn.commit()
            
            cursor = conn.cursor()
            sql = "select id,qw from table2 where 1=1"
            cursor.execute(sql)
            data = cursor.fetchall()
            for row in data:    
                id,qw = row
                message_out = '<b>'+str(id)+'</b>: '+str(qw)
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                keyboard.add(types.InlineKeyboardButton(text='delete', callback_data='delete_'+str(id))) 
                bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)
            save_status (user_id,username,'')                
                          
        if status == 'FIO': 
            message_out = 'Спасибо'
            bot.send_message(user_id,message_out,parse_mode='HTML')
            save_param (user_id,1,message)
            save_status (user_id,username,'agreg')
            message_out = 'Прошу Вас выслать фотографии документов с 2-х сторон:  стс. водительское удостоверение'
            bot.send_message(user_id,message_out,parse_mode='HTML')
    
        if status == 'agreg': 
            message_out = 'Спасибо'
            bot.send_message(user_id,message_out,parse_mode='HTML')
            save_param (user_id,2,message)
            save_status (user_id,username,'city')
            message_out = 'Прошу Вас выслать фотографии документов с 2-х сторон:  паспорт страница с фотографией'
            markup = menu_main ()
            bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)

        if status == 'city': 
            message_out = 'Спасибо'
            bot.send_message(user_id,message_out,parse_mode='HTML')
            save_param (user_id,3,message)
            save_status (user_id,username,'connect')
            message_out = 'Прошу Вас выслать фотографии документов с 2-х сторон:  Лицензия такси'
            markup = menu_main ()
            bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)

        if status == 'connect': 
            message_out = 'Спасибо'
            bot.send_message(user_id,message_out,parse_mode='HTML')
            save_param (user_id,4,message)
            save_status (user_id,username,'finish')
            markup = menu_main ()
            message_out = 'Прошу Вас выслать фотографии документов с 2-х сторон:  справка об отсутствии судимости.'
            bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
            markup = menu_main ()
            
        if status == 'finish':            
            message_out = 'Спасибо'
            bot.send_message(user_id,message_out,parse_mode='HTML')
            save_param (user_id,5,message)
            save_status (user_id,username,'')
            endfinish (user_id)



            
            
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        user_id = call.message.chat.id
        if call.data.find ("delete") != -1:
            codeglav = call.data.replace("delete_","" )
            print ('Удалить ',codeglav)
            
            conn = sqlite3.connect("qwest.sqlite") 
            cursor = conn.cursor()            
            cursor.execute("delete from table2 where id='"+str(codeglav)+"'")    
            conn.commit()
            message_out = 'Удален'
            markup = menu_main ()
            bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):

    user_id    = message.from_user.id 
    ##message    = message.text
    first_name = ''
    last_name  = ''
    username   = ''
    date       = ''
    status = load_staus (user_id)
 
    file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)      
    src = file_info.file_path;
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message,"Фото добавлено")    
    
    
    if 1==1:
        if status == 'agreg': 
            save_param (user_id,2,src)
            save_status (user_id,username,'city')
            message_out = 'Прошу Вас выслать фотографии документов с 2-х сторон:  паспорт страница с фотографией'
            markup = menu_main ()
            bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
            
        if status == 'city': 
            save_param (user_id,3,src)
            save_status (user_id,username,'connect')
            message_out = 'Прошу Вас выслать фотографии документов с 2-х сторон:  Лицензия такси'
            markup = menu_main ()
            bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)            
    
        if status == 'connect': 
            save_param (user_id,4,src)
            save_status (user_id,username,'finish')
            markup = menu_agreg ()
            message_out = 'Прошу Вас выслать фотографии документов с 2-х сторон:  справка об отсутствии судимости.'
            bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
          
        if status == 'finish':            
            save_param (user_id,5,src)
            save_status (user_id,username,'')
            endfinish (user_id)
         
            
bot.polling()















