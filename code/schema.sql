CREATE TABLE IF NOT EXISTS users 
                (id int auto_increment primary key,
                Full_name ,
                user_id UNIQUE NOT NULL, 
                purchases,
                lang
                );