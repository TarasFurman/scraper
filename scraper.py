import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.olx.ua/uk/obyavlenie/operativna-pamyat-dlya-noutbuka-ddr3-4gb-1600mhz-1-35v-IDEJIsX.html?sd=1#219ee306be'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('h1').get_text().strip()
    price = float(soup.find_all(
        'strong', {'class': 'xxxx-large not-arranged'})[0].get_text()[:-5])

    if price < 500:
        send_mail()

    print(title)
    print(price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('tarfurman@gmail.com', 'lriybwinuynahtlf')

    subject = 'Price fell down!'
    body = 'Check the olx link https://www.olx.ua/uk/obyavlenie/operativna-pamyat-dlya-noutbuka-ddr3-4gb-1600mhz-1-35v-IDEJIsX.html?sd=1#219ee306be'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'tarfurman@gmail.com',
        'tiger9249@gmail.com',
        msg
    )
    print("Hey Email is send")

    server.quit()


check_price()
