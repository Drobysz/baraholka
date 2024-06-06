buttons = {
    'spotify' : {
        'storage' : 'in',
        'buttons' : (
            ( 'Spotify Premium на 1 месяц', ' - 5 EUR 💵', 'pay spotify-1'),
            ('Spotify Premium на 6 месяцев', ' - 23 EUR 💵', 'pay spotify-6')
         ),
        'image' : 'images/Spotify_pr.png',
        'links' : ( 'code/subscriptions/spotify1.txt', 'code/subscriptions/spotify6.txt' )
    },
    'netflix' : {
        'storage' : 'in',
        'buttons' : ( ('Netflix 4K UHD на 3 месяца', ' -out of stock', '-'), ),
        'image' : 'images/Netflix_pr.png',
        'links' : ('code/subscriptions/netflix.txt',)
    },
    'ytprem' : {
        'storage' : 'in',
        'buttons' : ( ('YT Premium', ' -out of stock ', '-'), ) ,
        'image' : 'images/YT_pr.png', 
        'links' : ('code/subscriptions/ytprem.txt',)
    },
    'deezer' :  {
        'storage' : 'out',
        'buttons' : ('Deezer Premium 3 месяца', ' - 15 EUR 💵', 'pay deezer'),
        'image' : 'images/Deezer_pr.png'
    },
    'crunch' :  {
        'storage' : 'out',
        'buttons' : ('Crunchyroll Fan 3 месяца', ' - 14 EUR 💵', 'pay crunch'),
        'image' : 'images/Crunch_pr.jpg'
    },
    'paramount' :  {
        'storage' : 'out',
        'buttons' : ('Paramount+ Premium 3 месяца', ' - 15 EUR 💵', 'pay paramount'),
        'image' : 'images/Paramount_pr.jpg'
    },
    'office' :  {
        'storage' : 'out',
        'buttons' : ('Office 365 Personnel 3 месяца', ' - 15 EUR 💵', 'pay office'),
        'image' :  'images/Office_pr.png'
    }
}

platform_info = {
    'spotify' : '''🛒Товар: Spotify Individual
💲Цена: 6€

📑Описание: При покупке Spotify Premium, Вы получаете:
- Прослущивание музыка без рекламы
- Возможнсть скачивать музыку в любом качестве
- Выбор любого трека
''',
    'netflix' : '''🛒Товар: Netflix 4K UHD (1 person)
💲Цена: 5€

📑Описание: При покупке Netflix 4K UHD, Вы получаете:
- Неограниченное количество фильмов, телешоу и мобильных игр без рекламы
- Возможность смотреть фильмы в формате Full HD
- Возможность скачивать фильмы в Full HD
''',
    'ytprem' : '''🛒Товар: YouTube Premium 1 месяц
💲Цена: 5€

📑Описание: При покупке YouTube Premium, Вы получаете:
- Отсутствие рекламы
- Фоновый просмотр видео
- Безграничный доступ к YouTube Music
- Возможность скачивать видео в любом качестве
- Возможность скачивать трэки в YouTube Music
''',
    'deezer' : '''🛒Товар: Deezer Premium 3 месяца 
Цена: 15€

📑Описание: При покупке Deezer Premium, Вы получаете: 
-Отсутствие рекламы
-Возможнсть скачивать музыку в любом качестве
-Прослушивание музыки в качестве High Fidelity
''',
    'crunch' : '''🛒Товар: Crunchyroll Fan 3 месяца
Цена: 14€

📑Описание: При покупке Crunchyroll Fan, Вы получаете:
-Транслируйте всю библиотеку Crunchyroll без рекламы
 и смотрите новые серии вскоре после выхода в Японии
-Доступ только на 1 устройстве
''', 
    'paramount' : '''🛒Товар: Paramount+ Premium 3 месяца
 Цена: 15€

📑Описание: При покупке Paramount+ Premium , Вы получаете:
-Безграничный доступ ко всем фильмам и сериалам студии Paramount
-Отсутствие рекламы
''',
    'office' : '''🛒Товар: Office 365 Personnel 3 месяца
Цена: 15€

📑Описание: При покупке Office 365, Вы получаете: 
-Вход на пяти устройствах одновременно
-Облачное хранилище объемом 1 ТБ
Приложения с премиум-функциями и автономным доступом
 (Word, Excel,PowerPoint и т.д)
-Защищенная электронная почта без рекламы   
''', 
}

menu_text = {
    'tech_sup' : ''' По техническим вопросам обращайтесь к персоналу:
@mullerfaust
@gogonga'''}

review_text = {
    'review' : '''
Вы можете оставить отзыв или посмотреть отзывы других здесь : @planoise_comments

Для того, чтобы быть в курсе нового ассортимента
и обновлении в барахолке : @planoise_updates
'''}

answers = {
    'cloth' : '''
Чтобы вернуться в меню, нажмите кнопку "/menu", которая находится ниже.
Ожидайте ответа одного из наших операторов. Время ответа может занять
определенное время
''',
}

tarif_info = { 
    'spotify-1' : {
          'title' : 'Spotify',
          'description' : 'Item: Spotify 1 month Premium',
          'invoice_payload' : 'invoice-spotify-1',
          'photo_url' : 'https://www.promo-cines.com/2354-large_default/spotify-premium-e-carte-de-10-1-mois.jpg',
          'prices' : 5
    },
    'spotify-6' : {
          'title' : 'Spotify',
          'description' : 'Item: Spotify 6 month Premium',
          'invoice_payload' : 'invoice-spotify-6',
          'photo_url' : 'https://www.promo-cines.com/2354-large_default/spotify-premium-e-carte-de-10-1-mois.jpg',
          'prices' : 23
    },
    'netflix' : {
          'title' : 'Netflix',
          'description' : 'Item: 3 month Netflix 4K UHD',
          'invoice_payload' : 'invoice-netflix-3m-4k',
          'photo_url' : 'https://m.media-amazon.com/images/I/51LGj5--KsL.png',
          'prices' : 6   
    },
    'ytprem' : {
          'title' : 'YouTube Premium',
          'description' : 'Item: YouTube 1 month Premium',
          'invoice_payload' : 'invoice-ytprem-1m',
          'photo_url' : 'https://chromeunboxed.com/wp-content/uploads/2023/12/YouTubePremium.jpg?ezimgfmt=ng%3Awebp%2Fngcb114%2Frs%3Adevice%2Frscb115-1',
          'prices' : 6
    },
    'deezer' : {
          'title' : 'Deezer',
          'description' : 'Item: 3 month Deezer Premium',
          'invoice_payload' : 'invoice/deezer/3m',
          'photo_url' : 'https://m.media-amazon.com/images/I/51lo-v-XHZL.png',
          'prices' : 15  
    },
    'crunch' : {
          'title' : 'Crunchyroll',
          'description' : 'Item: 3 month Crunchryoll Fan',
          'invoice_payload' : 'invoice/crunchyroll/3m',
          'photo_url' : 'https://m.media-amazon.com/images/I/417bVUqe0pL.png',
          'prices' : 14   
    },
    'paramount' : {
          'title' : 'Paramount',
          'description' : 'Item: 3 month Paramount+ Premium',
          'invoice_payload' : 'invoice/paramount/3m',
          'photo_url' : 'https://m.media-amazon.com/images/I/717ZeBO09rL.png',
          'prices' : 15 
    },
    'office' : {
          'title' : 'Netflix',
          'description' : 'Item: 3 month Office 365 Personnel',
          'invoice_payload' : 'invoice/office365/3m',
          'photo_url' : 'https://backoffice.ccistore.fr/uploads/eservice/logo/1565176447080.jpg',
          'prices' : 15    
    }
}

