import requests
from bs4 import BeautifulSoup
from csv import writer

Page = 'https://egypt.souq.com/eg-en/lenovo-legion-5-gaming-laptop-intel-10th-gen-core-i7-15-6-inch-fhd-ips-backlit-keyboard-windows-10-phantom-black-131857743/i/'
response = requests.get(Page)
soup = BeautifulSoup(response.text, 'html.parser')
products = soup.findAll(class_='product_content')

with open('Products.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    Header = ['Page URL', 'Title', 'Brand' , 'Price', 'Sale', 'Image-Link']
    csv_writer.writerow(Header)

    for product in products:
        Title = product.find(class_='small-12 columns product-title').find('h1').get_text()
        Image = product.find(class_='img-bucket zoom-enabled').find('img')['src']
        Brand = product.find(class_='item-details-mini clearfix').find('ul').find('li').get_text().replace('Brand: ', '')
        Price = product.find(class_='price is sk-clr1').get_text().replace('\n', '').replace(' ', '')
        #Rating = product.find(class_='rate-of-avg').find('strong').get_text()                  ####Mesh Rady Yeshtaghal Ma3rafsh leh
        #Seller = product.find(class_='unit-seller-link').find('a').find('b').get_text()        ####Mesh Rady Yeshtaghal Ma3rafsh leh
        Sale = product.find(class_='discount').get_text().replace(' ', '').replace('off', '')

        csv_writer.writerow([Page, Title, Brand, Price, Sale, Image])