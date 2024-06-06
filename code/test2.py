a = 'https://www.journaldugeek.com/app/uploads/2021/07/template-jdg57.jpg'

import sqlite3 as sql3

conn = sql3.connect('users_db.sql')
cur = conn.cursor()

cur.execute('SELECT user_id from users')

user_list = cur.fetchall()

for user_id in user_list:
    cur.execute(f'SELECT {'num'+str(user_id[0])} FROM user_history')
    print(cur.fetchall())
    
cur.close()
conn.close()
