import telebot as tb
import config
import time as tm
import sqlite3 as sql3
import cloth_info as clinfo

bot = tb.TeleBot(config.TGRAM_DB_KEY)

conn = sql3.connect('users_db.sql')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS goods
            (id int auto_increment primary key,
            notes TEXT NOT NULL
          )''')
cur.execute('''CREATE TABLE IF NOT EXISTS number
            (id int auto_increment primary key,
            amount INTEGER DEFAULT 0
          )''')
cur.close()
conn.close()

@bot.message_handler(commands=['start','orders'])
def order_list(msg):
    
     
    conn = sql3.connect('users_db.sql')
    cur = conn.cursor()
    
    cur.execute('SELECT amount from number')
    last_ticket_amount = cur.fetchall()[0][0]
        
    tm.sleep(60)
    
    cur.execute('SELECT notes from goods')
    tickets = cur.fetchall()
    current_ticket_amount = len( tickets )
        
    if last_ticket_amount > current_ticket_amount:
       
       cur.close()
       conn.close()
        
       bot.send_message(msg.chat.id, 'Since your tickets history was changed or damaged, the program was suspended')
    
    elif last_ticket_amount == current_ticket_amount:
       
       cur.close()
       conn.close()
        
       order_list(msg)
        
    elif last_ticket_amount < current_ticket_amount:
       
       new_messages_amount = current_ticket_amount - last_ticket_amount
       new_tickets = tickets[-new_messages_amount:]
       
       poster = ''
       
       #   'invoice_cloth/'+cloth_type+'/'+mark+'/'+color+'/'+str(n_queue)+'/'+user_size+'/'+username+'/'+time  --- request
       #   country_code+'/'+state+'/'+city+'/'+street_line1+'/'+street_line2+'/'+post_code --- address
            
       for x in new_tickets:
           info = x[0].split('/')
           request = info[0]
           
           if request == 'invoice_cloth':
              cloth_type = info[1]
              mark = info[2]
              color = info[3]
              n_queue = int( info[4] )
              user_size = info[5]
              username = info[6]
              time = info[7]
              country_code = info[8]
              state = info[9]
              city = info[10]
              street_line1 = info[11]
              street_line2 = info[12]
              post_code = info[13]
              item = clinfo.types[cloth_type][mark][n_queue]
              
              poster = f'''@{username} купил {item['Name']} в {time} \n 
o----------Данные----------o
Название -- {item['Name']}
Тип одежды -- {cloth_type}
Марка -- {mark}
Цвет -- {color}
Размер -- {user_size}
o---------------------------------o

o----------Адрес----------o
Код страны -- {country_code}
Страна -- {state}
Город -- {city}
Адресная строка 1 : {street_line1}
Адресная строка 2 : {street_line2}
Почтовый код -- {post_code}
o---------------------------------o

    -------------- Cсылка на товар -------------- \n\n{item['Link']}
              '''
              
              image = open('cloth_images/'+cloth_type+'/'+mark+'/'+str(n_queue+1)+'/'+color+item['Photo_format'], 'rb')
               
              bot.send_photo(msg.chat.id, image, caption=poster)
                 
           elif request == 'sub':
              item = info[1]
              username = info[2]
              date = info[3]
              
              poster = f'@{username} made a purchase of {item} at {date} \n\n'
            
              bot.send_message(msg.chat.id, poster)
        
       cur.execute('UPDATE number SET amount = ? WHERE amount = ?', ( current_ticket_amount, last_ticket_amount ))
       conn.commit()
       
       cur.close()
       conn.close()
       
       order_list(msg) 


bot.polling(non_stop=True)