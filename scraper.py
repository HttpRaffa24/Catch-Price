import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = input('Paste the amazon product link here (Ctrl + V): ')
price_user = input('Enter the price below which the product should drop (Ex. 250.0): ')
receiver = input('Enter your email address here to receive price updates: ')

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])
    converted_price_user = float(price_user)

    print(title.strip())
    print(converted_price)


    if(converted_price < converted_price_user):
        send_email()



def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('username', 'password')                            #you have to generate app password google, then insert gmail and app password google

    subject = 'The price of the product you are looking for has gone down!!!'
    body = "Check the amazon link: ", URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '', #insert gmail to send the update
        'receiver',
        msg
    )

    print('Your email has just been sent!')

    server.quit()

while(True):
    check_price()
    time.sleep(3600)