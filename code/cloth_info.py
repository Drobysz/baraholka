links = {
    'Stonik' : 'https://hoobuy.com/product/2/7238464570?utm_source=share&utm_medium=product_details&inviteCode=QX19DDGX',
    'Kenzo' : 'https://www.allchinabuy.com/en/page/buy/?nTag=Home-search&from=search-input&_search=url&position=&url=https%3A%2F%2Fk.youshop10.com%2F5lm5NXg-&partnercode=ChinaB',
    'CP_shorts1' : 'https://hoobuy.com/product/0/746400723584?utm_source=share&utm_medium=product_details&inviteCode=QX1AVBkX',
    'PA_shorts1' : 'https://www.cssbuy.com/item-micro-7229597122.html?promotionCode=33f8c0870b3dd73a',
    'Moncler' : 'https://www.cssbuy.com/item-micro-7221837251.html?promotionCode=33f8c0870b3dd73a',
    'Denim Tears Shorts 1' : 'https://www.cssbuy.com/item-micro-7229516707.html?promotionCode=33f8c0870b3dd73a',
    'Stussy shorts 1' : 'https://www.cssbuy.com/item-micro-7226711522.html?promotionCode=33f8c0870b3dd73a',
    'Casablanca shirts' : 'https://hoobuy.com/product/1/681615258543?utm_source=share&utm_medium=product_details&inviteCode=QX1AVBkX',
    'Gucci cap' : 'https://www.cssbuy.com/item-micro-7231409533.html?promotionCode=33f8c0870b3dd73a',
    'Gucci bag' : 'https://hoobuy.com/product/2/7235075533?utm_source=share&utm_medium=product_details&inviteCode=QX1AVBkX',
    'Nike socks1' : 'https://www.cssbuy.com/item-micro-7226142749.html?promotionCode=33f8c0870b3dd73a',
    'Dior B30' : 'https://m.cssbuy.com//item-micro-7242490998.html', 
    'LV shoes1' : 'https://www.cssbuy.com/item-micro-7239272572.html?promotionCode=33f8c0870b3dd73a', 
}

# { '#' : 0, 'Name' : '', 'Info' : '', 'Btn_buy' : (), 'Photo' : (), 'Price' : 0, 'Link' : ''  }   --- образец БЗ товара

types = {
    't-shirts' : {
        'Stone Island' : ( 
            { '#' : 0,
             'Name' : 'Stone Island - Flame',
             'Btn_buy' : ('buy for ', ' 30 EUR 💵'),
             'Photo' :( { 'standard.jpeg', 'white.jpeg', 'beige.jpeg', 'blue.jpeg', 'gray.jpeg' } ),
             'Photo_format' : '.jpeg',
             'Price' : 30,
             'Price_orig' : '130-150 EUR 💵',
             'Link' : links['Stonik'],
             'Size' : 'S L M XL XXL'},
            { '#' : 1,
             'Name' : 'Stone Island - Standard',
             'Btn_buy' : ('buy for ', ' 30 EUR 💵'),
             'Photo' :( { 'standard.jpeg', 'white.jpeg', 'beige.jpeg', 'blue.jpeg', 'gray.jpeg' } ),
             'Photo_format' : '.jpeg',
             'Price' : 30,
             'Price_orig' : '130-150 EUR 💵',
             'Link' : links['Stonik'],
             'Size' : 'S L M XL XXL'},
            { '#' : 2,
             'Name' : 'Stone Island - Minimalism',
             'Btn_buy' : ('buy for ', ' 30 EUR 💵'),
             'Photo' :( { 'standard.jpeg', 'white.jpeg', 'beige.jpeg', 'blue.jpeg', 'gray.jpeg' } ),
             'Photo_format' : '.jpeg',
             'Price' : 30,
             'Price_orig' : '130-150 EUR 💵',
             'Link' : links['Stonik'],
             'Size' : 'S L M XL XXL' },
            ),
             
        #'Corteiz' : (),
        #'Under Armour' : (),
        'Casablanca' : (
            {
            '#' : 0,
            'Name' : 'Fenster Mini', 
            'Btn_buy' : ('buy for ', ' 25 EUR 💵'), 
            'Price' : 25,
            'Photo' : ( 'standard.jpeg', 'blue.jpeg', ),
            'Photo_format' : '.jpeg',
            'Link' : links['Casablanca shirts'],  
            'Size' : 'L M XL XXL XXXL',},
            
            {
            '#' : 1,
            'Name' : 'Avenida', 
            'Btn_buy' : ('buy for ', ' 25 EUR 💵'), 
            'Price' : 25,
            'Photo' : ( 'standard.jpeg', 'white.jpeg', ),
            'Photo_format' : '.jpeg',
            'Link' : links['Casablanca shirts'],  
            'Size' : 'L M XL XXL XXXL',},
            
            {
            '#' : 2,
            'Name' : 'Radiating Mushroom', 
            'Btn_buy' : ('buy for ', ' 25 EUR 💵'), 
            'Price' : 25,
            'Photo' : ( 'standard.jpeg', 'white.jpeg', ),
            'Photo_format' : '.jpeg',
            'Link' : links['Casablanca shirts'],  
            'Size' : 'L M XL XXL XXXL',},
            
            {
            '#' : 3,
            'Name' : 'Peace', 
            'Btn_buy' : ('buy for ', ' 25 EUR 💵'), 
            'Price' : 25,
            'Photo' : ( 'standard.jpeg', 'white.jpeg', ),
            'Photo_format' : '.jpeg',
            'Link' : links['Casablanca shirts'],  
            'Size' : 'L M XL XXL XXXL',},
            
            ),
        #'Moncler' : (),
        #'Off-White' : (),
        'Kenzo' : (
            { '#' : 0,
             'Name' : ' Kenzo Tiger',
             'Btn_buy' : ('buy for ', ' 30 EUR 💵'),
             'Photo' : ( 'black-gold.png', 'black-purple.png', 'blue.png', 'red.png', 'standard.png', ),
             'Photo_format' : '.png',
             'Price' : 30,
             'Price_orig' : '130-150 EUR 💵',
             'Link' : links['Kenzo'],
             'Size' : 'S L M XL XXL'},
            ),
        },
    'sneakers' : {
        'Dior' : (
            {
            '#' : 0,
            'Name' : 'B30', 
            'Btn_buy' : ('buy for ', ' 110 EUR 💵'), 
            'Price' : 110,
            'Photo' : ( 'standard.jpg', 'blue.jpg', 'rose.jpg', 'brown.jpg', 'dark-blue.jpg', ),
            'Photo_format' : '.jpg',
            'Link' : links['Dior B30'],  
            'Size' : '38 39 40 41 42 43 44 45',},
            ),
        'Louis Vuitton' : (
            {
            '#' : 0,
            'Name' : 'Basic', 
            'Btn_buy' : ('buy for ', ' 63 EUR 💵'), 
            'Price' : 110,
            'Photo' : ( 'standard.jpg', 'green.jpg', 'yellow.jpg', ),
            'Photo_format' : '.jpg',
            'Link' : links['LV shoes1'],  
            'Size' : '36 37 38 39 40 41 42 43 44',},
            ),
        },
    'socks' : {
        'Nike' : (
            {
            '#' : 0,
            'Name' : 'Medium', 
            'Btn_buy' : ('buy for ', ' 15 EUR 💵'), 
            'Price' : 15,
            'Photo' : ( 'standard.jpg', 'white.jpg', 'gray.jpg', ),
            'Photo_format' : '.jpg',
            'Link' : links['Nike socks1'],  
            'Size' : '34-38 38-42 43-46',},
            ),
        },
    'bags' : {
        'Gucci' : (
            {
            '#' : 0,
            'Name' : 'Viper', 
            'Btn_buy' : ('buy for ', ' 24 EUR 💵'), 
            'Price' : 24,
            'Photo' : ( 'standard.jpeg', 'viper.jpeg', 'gray.jpeg', ),
            'Photo_format' : '.jpeg',
            'Link' : links['Gucci bag'],  
            'Size' : 'None',},
            ),
        #'Louis Vuitton' : (),
        },
    'caps' : {
        #'Louis Vuitton' : (),
        'Gucci' : (
            {
            '#' : 0,
            'Name' : 'Standard', 
            'Btn_buy' : ('buy for ', ' 23 EUR 💵'), 
            'Price' : 23,
            'Photo' : ( 'standard.jpg', ),
            'Photo_format' : '.jpg',
            'Link' : links['Gucci cap'],  
            'Size' : 'None',},
            ),
        },
    'shorts' : {
        'Denim Tears' : (
            {
            '#' : 0,
            'Name' : 'Velvet', 
            'Btn_buy' : ('buy for ', ' 37 EUR 💵'), 
            'Price' : 37,
            'Photo' : ( 'standard.jpg', 'gray.jpg', 'light-blue.jpg', 'military.jpg', 'rose.jpg' ),
            'Photo_format' : '.jpg',
            'Link' : links['Denim Tears Shorts 1'],  
            'Size' : 'S L M XL',},
            ),
        'Palm Angeles' : (
            {
            '#' : 0,
            'Name' : 'Standard',
            'Btn_buy' : ('buy for ', ' 30 EUR 💵'),
            'Price' : 30,
            'Photo' : ( 'standard.jpg', 'white.jpg', 'light-blue.jpg'),
            'Photo_format' : '.jpg',    
            'Link' : links['PA_shorts1'],
            'Size' : 'S L M XL',},
            ),
        'Stussy' : (
            {
            '#' : 0,
            'Name' : 'Stusse Cubes',
            'Btn_buy' : ('buy for ', ' 28 EUR 💵'),
            'Price' : 28,
            'Photo' : ( 'standard.jpg', 'gray.jpg' ),
            'Photo_format' : '.jpg',
            'Link' : links['Stussy shorts 1'],    
            'Size' : 'M L XL XXl',},
            {
            '#' : 1,
            'Name' : 'Billiard Ball',
            'Btn_buy' : ('buy for ', ' 28 EUR 💵'),
            'Price' : 28,
            'Photo' : ( 'standard.jpg', 'gray.jpg' ),
            'Photo_format' : '.jpg',
            'Link' : links['Stussy shorts 1'],     
            'Size' : 'M L XL XXl',},
            {
            '#' : 2,
            'Name' : 'Nike Collab',
            'Btn_buy' : ('buy for ', ' 28 EUR 💵'),
            'Price' : 28,
            'Photo' : ( 'standard.jpg', 'gray.jpg' ),
            'Photo_format' : '.jpg', 
            'Link' : links['Stussy shorts 1'],    
            'Size' : 'M L XL XXl',},
            ),
        #'Corteiz' : (),
        #'R. Lauren' : (),
        'Moncler' : (
            {
            '#' : 0,
            'Name' : 'Summer vibe',
            'Btn_buy' : ('buy for ', ' 35 EUR 💵'),
            'Price' : 35,
            'Photo' : ( 'standard.jpg', 'rose.jpg', 'white.jpg', 'red.jpg', 'black-red.jpg', 'light-blue.jpg', ),
            'Photo_format' : '.jpg',  
            'Link' : links['Moncler'],   
            'Size' : 'M L XL XXl',},
            ),
        #'Balenciaga' : (),
        'CP Company' : (
            {
            '#' : 0,  
            'Name' : 'Standard',
            'Btn_buy' : ('buy for ', ' 30 EUR 💵'),
            'Price' : 30,
            'Photo' : ( 'standard.jpg', 'gray.jpg',  'military.jpg',  'light-green.jpg', ),
            'Photo_format' : '.jpg',  
            'Link' : links['CP_shorts1'],
            'Size' : 'L M XL XXL',},
            ),
        },
}

sizes = {
    't-shirts' : 'S L M XL XXL',
    'sneakers' : '40 41 41.5 42 42.5 43.5 44 45' 
}

