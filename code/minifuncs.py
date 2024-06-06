import deepl
import config
import sqlite3 as sql3

translator = deepl.Translator(config.DPL_KEY)


def interpetate(text, lang):
    
    translated = translator.translate_text( text, target_lang=lang )
    
    return str(translated)


def part_of_time(hour):
    
    if hour < 11 and hour >= 6 :
        hour = 'morning'
    elif hour == 12 :
        hour = 'noon'
    elif hour >= 13 and hour <= 16 :
        hour = 'afternoon'
    elif hour >= 17 and hour <= 20:
        hour = 'evening'
    else:
        hour = 'night'
    
    return hour


def define_lang( id ):
    conn = sql3.connect('users_db.sql')
    cur = conn.cursor()
    cur.execute(f'SELECT lang FROM users WHERE user_id={id}')
    
    data = cur.fetchall()
    lang = data[0][0]
    cur.close()
    conn.close()
    
    return lang


def change_lang( user_id, new_lang ):
    
    conn = sql3.connect('users_db.sql')
    cur = conn.cursor()
    data = (new_lang, user_id)
    cur.execute('UPDATE users SET lang = ? WHERE user_id = ?', data)
    conn.commit()
    cur.close()
    conn.close()
    

def show_users():
    
    conn = sql3.connect('users_db.sql')
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM users')
    
    data = cur.fetchall()
    print(f' DATA ------ {data}')

    cur.close()
    conn.close()
    

def user_history(user_id):
    
    conn = sql3.connect('users_db.sql')
    cur = conn.cursor()
    cur.execute(f'SELECT {'num'+str(user_id)} FROM user_history')
    history = cur.fetchall()
    cur.close()
    conn.close()
    
    return history
    