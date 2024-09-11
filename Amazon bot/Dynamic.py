import requests as r
from bs4 import BeautifulSoup
import smtplib
import lxml
base_url = 'https://www.amazon.in'
url = 'https://www.amazon.in/dp/B0CY5HVDS2'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}
base_response = r.get(base_url, headers=headers)
cookies = base_response.cookies
product_response = r.get(url, headers=headers, cookies=cookies)
soup = BeautifulSoup(product_response.text, 'lxml')
price = soup.find(name="span", class_="a-price-whole")
price_as_int = int(price.text.replace(",", "").replace(".", ""))
title = soup.find(name="span", id="productTitle").get_text().strip()
subject = "Price Alert!"
body = f"{title} is available at ₹{price_as_int:.2f}"
message = f"Subject: {subject}\n\n{body}"
message = message.encode('utf-8')
if price_as_int < 55000:
    my_email = "toastedcheese146@gmail.com"
    password = "cnib wpnh pacr kbjd"
    try:

        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="ali.221204.co@mhssce.ac.in", msg=message)
        connection.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
print(f"Price: ₹{price_as_int}")
