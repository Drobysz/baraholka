import telebot as tb
from telebot import types as tp
import config
import time as tm
import sqlite3 as sql3
import minifuncs as minif
import platforms_info as pinfo
import cloth_info as clinfo

bot = tb.TeleBot(config.TGRAM_KEY)

conn = sql3.connect('users_db.sql')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users 
                (id int auto_increment primary key,
                Full_name ,
                user_id UNIQUE NOT NULL, 
                purchases,
                lang
                )''')
cur.execute('''CREATE TABLE IF NOT EXISTS user_history 
                (id int auto_increment primary key,
                LOL NOT NULL
                )''')
cur.close()
conn.close()

@bot.message_handler(commands=['start']) 
def id_handler(msg):
    
    global conn, cur, user_id
    
    conn = sql3.connect('users_db.sql')
    cur = conn.cursor()
    cur.execute(f'SELECT user_id FROM users WHERE user_id={msg.from_user.id}')
    user_id = cur.fetchall()
    
    if user_id == []:
        
        cur.close()
        conn.close()
        print('USER_ID ---- ', user_id)    
        markup = tp.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        btn1 = tp.KeyboardButton('English')
        btn2 = tp.KeyboardButton('Français')
        btn3 = tp.KeyboardButton('Русский')
        btn4 = tp.KeyboardButton('Український')
        btn5 = tp.KeyboardButton('العربية')

        markup.add(btn1, btn2, btn3, btn4, btn5)
    
        hour = minif.part_of_time(tm.localtime().tm_hour)
        full_name = str(msg.from_user.username)
        
        bot.send_message( msg.chat.id, f'Good {hour}, {full_name}! Choose your language ' ,reply_markup=markup )
        
        bot.register_next_step_handler(msg, set_lang)
    
    else:
        
        conn = sql3.connect('users_db.sql')
        cur = conn.cursor()

        cur.execute(f'SELECT lang, full_name FROM users WHERE user_id={msg.from_user.id}')
        data = cur.fetchall()
        full_name = data[0][1]
        lang = data[0][0]
        text = [ 'Go to the menu', f' {full_name} , Do you wish to go to the menu ? ' ]
        markup = tp.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        markup.add(tp.KeyboardButton(minif.interpetate( text[0], lang )))
        bot.send_message( msg.chat.id, minif.interpetate( text[1], lang ), reply_markup=markup )
        cur.close()
        conn.close()
        
        
        bot.register_next_step_handler(msg, menu)
            
        
def set_lang(msg):
     
    global  conn, cur
    lang = ''

    if msg.text == 'English':
        lang = 'EN-US'
    elif msg.text == 'Français':
        lang = 'FR'
    elif msg.text == 'Русский':
        lang = 'RU' 
    elif msg.text == 'Український':
        lang = 'UK'
    elif msg.text == 'العربية':
        lang = 'AR' 
             
    
    if lang != '': 
             
       f_name = str(msg.from_user.username)  
       data = (f_name, msg.from_user.id, lang) 
       print('REGISTRATED_USER_DATA ------ ',data) 
       
       conn = sql3.connect('users_db.sql')
       cur = conn.cursor() 
       cur.execute('INSERT INTO users (Full_name, user_id, lang) VALUES(?, ?, ?)', data)
       conn.commit()
       
       # addition of purchase history column
       cur.execute(f"ALTER TABLE user_history ADD COLUMN {'num'+str(msg.from_user.id)} TEXT")
       conn.commit()
       
       cur.close()
       conn.close()
       
       markup = tp.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
       markup.add(tp.KeyboardButton(minif.interpetate('Go to the menu', lang)))
       bot.send_message( msg.chat.id, minif.interpetate(f' {f_name} , Do you wish to go to the menu ? ', lang) ,reply_markup=markup )
        
       bot.register_next_step_handler(msg, menu)


@bot.message_handler(commands=['menu'])
def menu(msg):
    
    lang = minif.define_lang( msg.from_user.id )
    
    markup = tp.InlineKeyboardMarkup()
    
    btn1 = tp.InlineKeyboardButton(minif.interpetate('Subscriptions to services', lang)+' 🛒', callback_data='shop')
    btn2 = tp.InlineKeyboardButton(minif.interpetate('Tech Support', lang)+'🛠', callback_data='tech')
    btn3 = tp.InlineKeyboardButton(minif.interpetate('Guide to use (-)', lang)+' 📒', callback_data='guide')
    btn4 = tp.InlineKeyboardButton(minif.interpetate('Client reviews', lang)+' 📢', callback_data='reviews')
    btn5 = tp.InlineKeyboardButton(minif.interpetate('Purchases history', lang)+' 💼', callback_data='history')
    btn6 = tp.InlineKeyboardButton(minif.interpetate('Language', lang)+' 🗣', callback_data='lang')
    btn7 = tp.InlineKeyboardButton(minif.interpetate('Clothing shop (soon)', lang)+' 👕', callback_data='cloth')
    
    markup.row(btn1)
    markup.row(btn7)
    markup.row(btn6, btn4)
    markup.row(btn2, btn5)
    markup.row(btn3)
    
    image = open('images/menu.jpeg', 'rb')
    
    bot.send_photo( msg.chat.id,photo=image,caption=minif.interpetate('Menu of the Shop', lang) ,reply_markup=markup )


@bot.pre_checkout_query_handler(lambda query: True)
def checkout_precessing(query=tp.PreCheckoutQuery):
    bot.answer_pre_checkout_query(query.id, ok=True)


@bot.message_handler(content_types=['successful_payment'])
def payment(msg):
    
    lang = minif.define_lang( msg.chat.id )
    
    invoice = msg.successful_payment.invoice_payload.split('/')[0]
    #   'invoice_cloth/'+cloth_type+'/'+mark+'/'+color+'/'+str(n_queue)+'/'+user_size  --- request
    
    lines = []
    lamp = 0
    if msg.successful_payment.invoice_payload == 'invoice-spotify-1':
       url = 'code/subscriptions/spotify.txt'
       item = 'Spotify 1 month'
       lamp = 1
    elif msg.successful_payment.invoice_payload == 'invoice-netflix-3m-4k':
       url = 'code/subscriptions/netflix.txt'
       item = 'Netflix 3 month'   
       lamp = 1
    elif msg.successful_payment.invoice_payload == 'invoice-ytprem-1m':
       url = 'code/subscriptions/ytprem.txt' 
       item = 'YouTube Premium 1 month'
       lamp = 1
      
    if lamp == 1: 
       with open(url, 'r') as f:
            lines = f.readlines()
    
    if lines != []:      
       bot.send_message(msg.chat.id, minif.interpetate('Your item :', lang)+' '+lines[-1].strip())
       
       with open(url, 'w') as f:
            f.writelines(lines[:-1])  
          
    else: 
    
       conn = sql3.connect('users_db.sql')
       cur = conn.cursor()
       
       if invoice == 'invoice_cloth' :
           user_address = msg.successful_payment.order_info.shipping_address
           # address data
           
           country_code = user_address.country_code
           state = user_address.state
           city = user_address.city
           street_line1 = user_address.street_line1
           if user_address.street_line2 != '':
              street_line2 = user_address.street_line2
           else:
              street_line2 = 'Non written'  
           post_code = user_address.post_code

           address_string = country_code+'/'+state+'/'+city+'/'+street_line1+'/'+street_line2+'/'+post_code
           
           response = 'Our operators will respond to you soon. If you don\'t get a response for a long time, you can contact @mullerfaust'
           purchase_info = msg.successful_payment.invoice_payload+'/'+msg.from_user.username+'/'+tm.strftime( '%H:%M:%S %A-%B-%Y' )+'/'+address_string

       else: 
          response = 'The product is currently missing from the storage. However, our team will try to deliver it to you as soon as possible' 
          print(msg.successful_payment.invoice_payload)
          item = msg.successful_payment.invoice_payload.split('/')[1]
          purchase_info = 'sub/'+item+'/'+msg.from_user.username+'/'+tm.strftime( '%H:%M:%S %A-%B-%Y' )
       
       bot.send_message(msg.chat.id, minif.interpetate(response, lang))   
       cur.execute('INSERT INTO goods (notes) VALUES(?)', (str(purchase_info),))
       conn.commit()  
       
       cur.execute(f'INSERT INTO user_history ({'num'+str(msg.from_user.id)}) VALUES(?)', ( str(purchase_info), ) )
       conn.commit()
       cur.close()
       conn.close()
       
        
@bot.callback_query_handler(func=lambda call:True)
def menu_handler(call):
    
    lang = minif.define_lang( call.message.chat.id )
    
    # Subscriptions menu
    
    if call.data == 'shop' or call.data == 'back sub' :
    
       subs_text = '''
        There're available subscriptions on following platforms
       '''
       markup = tp.InlineKeyboardMarkup(row_width=1)
       btn1 = tp.InlineKeyboardButton('🟢 '+' Spotify '+' 🟢', callback_data='sub spotify')
       btn2 = tp.InlineKeyboardButton('🔴 '+' Netflix (soon) '+' 🔴', callback_data='sub netflix')
       btn3 = tp.InlineKeyboardButton('♦️'+' Youtube Premium(soon) '+'♦️', callback_data='sub ytprem')
       btn4 = tp.InlineKeyboardButton('🟣 '+' Deezer '+' 🟣', callback_data='sub deezer')
       btn5 = tp.InlineKeyboardButton('🟠 '+ ' Crunchyroll '+' 🟠', callback_data='sub crunch')
       btn6 = tp.InlineKeyboardButton('🔵 '+' Paramount '+' 🔵', callback_data='sub paramount')
       btn7 = tp.InlineKeyboardButton('⚪ '+' Office 365 '+' ⚪', callback_data='sub office')
       
       back = tp.InlineKeyboardButton( minif.interpetate('back', lang)+'⬅️', callback_data='back menu' )
    
       markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, back)
       
       image = open('images/submenu.png', 'rb')
       
       bot.edit_message_media(
           chat_id=call.message.chat.id,
           message_id= call.message.id,
           media=tp.InputMediaPhoto( image ,caption=minif.interpetate(subs_text, lang)),
           reply_markup=markup
       )
    
    lang_check = call.data.split(' ')
       
    # Menu 
   
    if call.data == 'back menu' or lang_check[0] == 'l' : 
       
       if lang_check[0] == 'l':
         
          minif.change_lang( call.message.chat.id, lang_check[1] )
       
          lang = lang_check[1]
       
       markup = tp.InlineKeyboardMarkup()
    
       btn1 = tp.InlineKeyboardButton(minif.interpetate('Subscriptions to services', lang)+' 🛒', callback_data='shop')
       btn2 = tp.InlineKeyboardButton(minif.interpetate('Tech Support', lang)+' 🛠', callback_data='tech')
       btn3 = tp.InlineKeyboardButton(minif.interpetate('Guide to use (-)', lang)+' 📒', callback_data='guide')
       btn4 = tp.InlineKeyboardButton(minif.interpetate('Client reviews', lang)+' 📢', callback_data='reviews')
       btn5 = tp.InlineKeyboardButton(minif.interpetate('Purchases history', lang)+' 💼', callback_data='history')
       btn6 = tp.InlineKeyboardButton(minif.interpetate('Language', lang)+' 🗣', callback_data='lang')
       btn7 = tp.InlineKeyboardButton(minif.interpetate('Clothing shop (soon)', lang)+' 👕', callback_data='cloth')
    
       markup.row(btn1)
       markup.row(btn7)
       markup.row(btn6, btn4)
       markup.row(btn2, btn5)
       markup.row(btn3)
       
       image = open('images/menu.jpeg', 'rb')
       
       bot.edit_message_media(
           chat_id=call.message.chat.id,
           message_id= call.message.id,
           media=tp.InputMediaPhoto( image ,caption=minif.interpetate('Menu of the Shop', lang)),
           reply_markup=markup
       )
    
    # Cloth shop
    
    if call.data == 'cloth':
        
       markup = tp.InlineKeyboardMarkup()
       
       image = open('images/clothmenu.jpg', 'rb')
       
       t_shirts = tp.InlineKeyboardButton(minif.interpetate('t-shirts', lang), callback_data='cloth t-shirts')
       sneakers = tp.InlineKeyboardButton(minif.interpetate('sneakers', lang), callback_data='cloth sneakers')
       socks = tp.InlineKeyboardButton(minif.interpetate('socks', lang), callback_data='cloth socks')
       bags = tp.InlineKeyboardButton(minif.interpetate('bags', lang), callback_data='cloth bags')
       caps = tp.InlineKeyboardButton(minif.interpetate('hats and caps', lang), callback_data='cloth caps')
       shorts = tp.InlineKeyboardButton(minif.interpetate('shorts', lang), callback_data='cloth shorts')
       
       back = tp.InlineKeyboardButton( minif.interpetate('back', lang)+'⬅️', callback_data='back menu' )
       
       markup.row( t_shirts, sneakers )
       markup.row( socks, shorts )
       markup.row( caps, bags )
       markup.row( back )
       
       bot.edit_message_media(
           chat_id=call.message.chat.id,
           message_id=call.message.id,
           media=tp.InputMediaPhoto( image ,caption=minif.interpetate('High quality сlothing Store', lang)),
           reply_markup=markup
       )
       
    # Cloth brands
    
    request = call.data.split(' ')
    
    if  len( request ) > 1 and request[0] == 'cloth':
        
        #  тип товара
        cloth_type = request[1]
        markup = tp.InlineKeyboardMarkup()
        
        image = open( 'images/brandmenu.jpeg', 'rb' )
        
        #  массив с названиями марок в катологе 
        
        for mark in clinfo.types[cloth_type].keys():
            
            search = 'catalog/' + cloth_type + '/' + mark + '/standard/0' 
            mark_btn = tp.InlineKeyboardButton( mark, callback_data = search )
            markup.row(mark_btn)
        
        #  кнопки back и back menu
            
        back = tp.InlineKeyboardButton( minif.interpetate('back', lang)+'⬅️', callback_data='cloth' )
        back_to_menu = tp.InlineKeyboardButton( minif.interpetate('back to menu', lang)+'🔚', callback_data='back menu' )
        markup.row( back, back_to_menu )
        
        #  вывод странички
            
        bot.edit_message_media(
           chat_id=call.message.chat.id,
           message_id=call.message.id,
           media=tp.InputMediaPhoto( image ,caption=minif.interpetate('List of brands', lang)),
           reply_markup=markup
       )
        
    # Brand item menu
    
    request = call.data.split('/')

    if request[0] == 'catalog':
        
        #  регистрация данных : тип одежды - марка - цвет - текущая стр - каталог товаров определенной марки - товар на тек. стр.    
        cloth_type = request[1]
        mark = request[2]
        color = request[3]
        n_queue = int( request[4] ) 
        catalog = clinfo.types[cloth_type][mark]
        total_amount = len( catalog )
        item = catalog[n_queue]
        
        markup = tp.InlineKeyboardMarkup()
        
        #         Образец запроса ---- 'catalog/' + cloth_type + '/' + mark + '/' + color + '/' + str( n_queue )
        
        #  Регистрация кнопок  < page > 
        if item['Size'] != 'None':
           buy_request = 'pay_info/'+cloth_type+'/'+mark+'/'+color+'/'+str(n_queue)
        else:
           buy_request = 'pay_cloth/'+cloth_type+'/'+mark+'/'+color+'/'+str(n_queue)+'/None'
            
        btn_buy = tp.InlineKeyboardButton( minif.interpetate( item['Btn_buy'][0], lang ) + item['Btn_buy'][1] , callback_data=buy_request )
        page = str( n_queue + 1 ) + '/' + str( total_amount )
        page_btn = tp.InlineKeyboardButton( page, callback_data='-'  )
        
        markup.row(btn_buy)
        
        #  Кнопки с доступными цветами
        
        btn_good = tp.InlineKeyboardButton('🔴-🔵-🟣 ' + minif.interpetate( 'COLORS', lang) + ' ⚪️-🟡-🟢', callback_data='-' )
        markup.row(btn_good)
        
        for file in item['Photo'] :
            
            paint = file.split('.')[0]
            
            if paint != color:
                search = 'catalog/' + cloth_type + '/' + mark + '/' + paint + '/' + str( n_queue )
                
            else:
                search = '-'
                paint = 'o----> ' + paint + ' <----o'
            
            btn_paint = tp.InlineKeyboardButton( paint, callback_data = search )
            markup.add(btn_paint)

        #  Условие появление кнопок < page >
        
        search_left = 'catalog/' + cloth_type + '/' + mark + '/' + color + '/' + str(n_queue-1)
        search_right = 'catalog/' + cloth_type + '/' + mark + '/' + color + '/' + str(n_queue+1)
        
        if n_queue - 1 < 0:
           search_left = '-'
            
        elif n_queue + 1 == total_amount:
           search_right = '-'   
           
        left = tp.InlineKeyboardButton( '<', callback_data = search_left ) 
        right = tp.InlineKeyboardButton( '>', callback_data = search_right )
        
        markup.row(left, page_btn, right)

        #  Список товаров
        
        btn_good = tp.InlineKeyboardButton('---' + minif.interpetate( 'goods', lang).upper() + '---', callback_data='-' )
        markup.row(btn_good)
        
        for good in catalog:

            if good['#'] != n_queue:
                btn_text = '🔵  ' + good['Name'] + ' 🔵'
                search = 'catalog/' + cloth_type + '/' + mark + '/standard/' + str( good['#'] )
                
            else:
                btn_text = '🔴 ' + good['Name'] + ' 🔴'
                search = '-'
                
            btn_good = tp.InlineKeyboardButton( btn_text, callback_data=search )
            markup.add(btn_good)

        #  Кнопки back и back menu
        
        back_text = 'cloth ' + cloth_type    
        back = tp.InlineKeyboardButton( minif.interpetate('back', lang)+'⬅️', callback_data=back_text )
        back_to_menu = tp.InlineKeyboardButton( minif.interpetate('back to menu', lang)+'🔚', callback_data='back menu' )
        markup.row( back, back_to_menu )    
        
        #  Вывод данных
        
        image = open('cloth_images/'+cloth_type+'/'+mark+'/'+str(n_queue+1)+'/'+color+item['Photo_format'], 'rb')
        text = minif.interpetate(item['Name'], lang)
        
        if item['Size'] != 'None':
            
            text += '\n\n--- Размерный ряд ---\n\n' + item['Size']

        bot.edit_message_media(
           chat_id=call.message.chat.id,
           message_id=call.message.id,
           media=tp.InputMediaPhoto( image ,caption=text ),
           reply_markup=markup
       )
        
    # Services info
  
    subs = call.data.split(' ')
    
    if subs[0] == 'sub':
        
      markup = tp.InlineKeyboardMarkup()
      item_data = pinfo.buttons[subs[1]]
      item_amount = 0
      reminder = ''
      
      if item_data['storage'] == 'out' : 
         
         btns = item_data['buttons']
         btn =  tp.InlineKeyboardButton( minif.interpetate(btns[0], lang)+btns[1], callback_data = btns[2] )
         markup.row(btn)
         
         text = pinfo.platform_info[subs[1]]
         
      elif item_data['storage'] == 'in':
         
         for btns in item_data['buttons']:
             
             btn = tp.InlineKeyboardButton( minif.interpetate(btns[0], lang)+btns[1], callback_data = btns[2] )
             markup.row(btn)
             
         for link in item_data['links']:
 
             with open(link, 'r') as f:                 
                  item_amount += len( f.readlines() )
         
         if item_amount == 0:
             reminder = '⚠️   ----------------------------------------\nReminder: even if the product is out of stock, you can purchase it,just the product will be delivered a little later'
             
         text = pinfo.platform_info[subs[1]] + '\n\nItems :' + str(item_amount) + '📦\n' + reminder
      
      image = open( item_data['image'], 'rb' )
          
      back = tp.InlineKeyboardButton( minif.interpetate('back', lang)+'⬅️', callback_data='back sub' )
      back_to_menu = tp.InlineKeyboardButton( minif.interpetate('back to menu', lang)+'🔚', callback_data='back menu' )
      markup.row( back, back_to_menu )
        
      bot.edit_message_media(
          chat_id=call.message.chat.id,
          message_id= call.message.id,
          media=tp.InputMediaPhoto( image ,caption=text ),
          reply_markup=markup
        )   
      
    # Change language 
    
    if call.data == 'lang':
      
      markup = tp.InlineKeyboardMarkup(row_width=1)
      
      btn1 = tp.InlineKeyboardButton('English🇬🇧', callback_data='l EN-US')
      btn2 = tp.InlineKeyboardButton('Français🇫🇷', callback_data='l FR')
      btn3 = tp.InlineKeyboardButton('Русский🇷🇺', callback_data='l RU')
      btn4 = tp.InlineKeyboardButton('Український🇺🇦', callback_data='l UK')
      btn5 = tp.InlineKeyboardButton('🇦🇪 العربية', callback_data='l AR')
      back = tp.InlineKeyboardButton( minif.interpetate('back', lang)+'⬅️', callback_data='back menu' )

      markup.add(btn1, btn2, btn3, btn4, btn5, back)
      
      image = open('images/lang.jpeg', 'rb')
      
      bot.edit_message_media(
           chat_id=call.message.chat.id,
           message_id= call.message.id,
           media=tp.InputMediaPhoto( image ,caption=minif.interpetate( ' Choose your language ', lang )),
           reply_markup=markup
        ) 
         
    # Tech support  
      
    if  call.data == 'tech':
        
        markup = tp.InlineKeyboardMarkup()
        back = tp.InlineKeyboardButton( minif.interpetate('back', lang)+'⬅️', callback_data='back menu' )
        markup.add(back)
        
        text = pinfo.menu_text['tech_sup']    
        image = open('images/techsup2.jpeg', 'rb')

        bot.edit_message_media(
           chat_id=call.message.chat.id,
           message_id= call.message.id,
           media=tp.InputMediaPhoto( image ,caption=minif.interpetate( text, lang )),
           reply_markup=markup
        ) 
    
    # Purchases history 
     
    if call.data == 'history' :
        data = minif.user_history(call.message.chat.id)
        history = '-----Your purchases for all time-----'
        
        if data[0][0] != None :
           
           for item_string in data:
               
               item = item_string[0].split('/')
               
               #   'invoice_cloth/'+cloth_type+'/'+mark+'/'+color+'/'+str(n_queue)+'/'+user_size  --- request 
               if item[0] == 'invoice_cloth':
                  
                  cloth_type = item[1]
                  mark = item[2]
                  color = item[3]
                  n_queue = int(item[4])
                  user_size = item[5]
                  item_data = clinfo.types[cloth_type][mark][n_queue]
                  
                  history += f'''
o----------------INFO----------------o
Name --- {item_data['Name']}
Clothing type --- {cloth_type}
Brand --- {mark}
Color --- {color}
Size --- {user_size}
o----------------------------------------o\n\n''' 
               else:
                   item = item[1]
                   date = item[3]
                   history = f'You made a purchase of {item} at {date} \n\n'
                
        else:
           
           history = "You hasn't yet purchased anything" 
           
        image = 'images/history.jpeg'        
        markup = tp.InlineKeyboardMarkup()
        back = tp.InlineKeyboardButton( minif.interpetate('back', lang)+'⬅️', callback_data='back menu' )
        markup.add(back)   
           
        bot.edit_message_media(
           chat_id=call.message.chat.id,
           message_id= call.message.id,
           media=tp.InputMediaPhoto( open( image, 'rb' ) ,caption=minif.interpetate( history, lang )),
           reply_markup=markup
       )
    
    # Reviews
    
    if call.data == 'reviews':
        
        markup = tp.InlineKeyboardMarkup()
        back = tp.InlineKeyboardButton( minif.interpetate('back', lang)+'⬅️', callback_data='back menu' )
        markup.add(back)
        
        text_review_page = pinfo.review_text['review']
        image = open('images/reviews.png', 'rb')
        
        bot.edit_message_media(
           chat_id=call.message.chat.id,
           message_id= call.message.id,
           media=tp.InputMediaPhoto( image ,caption=minif.interpetate( text_review_page, lang )),
           reply_markup=markup
        )
    
    # Payment processing subscriptions
    
    pay = call.data.split(' ')
       
    if pay[0] == 'pay':
        
        markup = tp.InlineKeyboardMarkup(row_width=1)
        payment = tp.InlineKeyboardButton('pay', pay=True) 
        markup.add(payment)
        
        service_key = pay[1]
        pay_info = pinfo.tarif_info[service_key]

        bot.send_invoice( call.message.chat.id,
                        title = pay_info['title'],
                        description = pay_info['description'],
                        invoice_payload = pay_info['invoice_payload'],
                        provider_token = config.STRIPE_TEST_KEY, 
                        currency ='EUR',
                        prices = [tp.LabeledPrice(pay_info['title'], pay_info['prices'] * 100)], 
                        photo_url = pay_info['photo_url'],
                        photo_height = 300, 
                        photo_width = 300,   
                        photo_size = 512,
                        reply_markup = markup
                    )

        markup_reply = tp.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup_reply.row( tp.KeyboardButton('/menu') )
        
        bot.send_message(call.message.chat.id,
                         text=minif.interpetate('Чтобы вернуться в меню, нажмите кнопку "/menu", которая находится ниже', lang),
                         reply_markup=markup_reply
                     )
        
    # Choice of size
    
    pay = call.data.split('/')
    
    if pay[0] == 'pay_info':
        
        # 'pay_info/'+cloth_type+'/'+mark+'/'+color+'/'+str(n_queue)
        cloth_type = pay[1]
        mark = pay[2]
        n_queue = int(pay[4])
        sizes = clinfo.types[cloth_type][mark][n_queue]['Size'].split(' ')
        request = call.data[9:]
        markup = tp.InlineKeyboardMarkup()
        image = open( 'images/size.jpg', 'rb')
        
        for size in sizes:
            size_btn = tp.InlineKeyboardButton( size, callback_data= 'pay_cloth/' + request + '/' + size )
            markup.add(size_btn)
            
        text = 'Выберете ваш размер'    
        
        back_text = 'catalog/' + request
        back = tp.InlineKeyboardButton( minif.interpetate('back', lang)+'⬅️', callback_data=back_text )
        back_to_menu = tp.InlineKeyboardButton( minif.interpetate('back to menu', lang)+'🔚', callback_data='back menu' )
        markup.row(back, back_to_menu)
            
        bot.edit_message_media(
           chat_id=call.message.chat.id,
           message_id=call.message.id,
           media=tp.InputMediaPhoto( image ,caption=minif.interpetate( text, lang ) ),
           reply_markup=markup
        )
            
    # Payment processing cloth
    
    if pay[0] == 'pay_cloth':
        
        # 'pay_cloth/'+cloth_type+'/'+mark+'/'+color+'/'+str(n_queue)+'/'+size
        cloth_type = pay[1]
        mark = pay[2]
        color = pay[3]
        n_queue = int(pay[4])
        user_size = pay[5]
        photo_url = 'https://andrearugg.com/wp-content/uploads/2015/06/CashRegisters1_2015_11_19.jpg'
        item = clinfo.types[cloth_type][mark][n_queue]
        markup = tp.InlineKeyboardMarkup(row_width=1)
        invoice_request = 'invoice_cloth/'+cloth_type+'/'+mark+'/'+color+'/'+str(n_queue)+'/'+user_size
        description = f'Your size : {user_size}\n, Your color : {color}\nApproximate delivery time : 3 - 5 weeks' 
                            
        
        bot.send_invoice( call.message.chat.id,
                        title = item['Name'],
                        description = description,
                        invoice_payload = invoice_request,
                        provider_token = config.STRIPE_TEST_KEY, 
                        currency ='EUR',
                        prices = [tp.LabeledPrice(item['Name'] ,item['Price'] * 100)], 
                        photo_url = photo_url,
                        photo_height = 300, 
                        photo_width = 500,   
                        photo_size = 512,
                        reply_markup = markup,
                        need_shipping_address=True,
                    )
        
        markup_reply = tp.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup_reply.row( tp.KeyboardButton('/menu') )
        
        bot.send_message(call.message.chat.id,
                         text=minif.interpetate(pinfo.answers['cloth'], lang),
                         reply_markup=markup_reply
                     )
       
    
bot.infinity_polling()
      
      
