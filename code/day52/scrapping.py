#scrapping to track price in amazon
from bs4 import BeautifulSoup
import requests
import lxml

url = "https://www.amazon.in/Acer-i5-12500H-Processor-Graphics-AN515-58/dp/B09WN8FF5T?th=1"
#put your header here , you should put user-agen, accept-language compulsory
header = "you can generate header by www.myhttpheader.com"
r = requests.get(url, headers=header)
soup = BeautifulSoup(r.text, "lxml")
price = soup.find(name="p", class_="a-spacing-none a-text-left a-size-mini twisterSwatchPrice")
price_filtered = price.text.split("₹")[1] # without string
price_filtered2 = price_filtered.split(",")[0]+price_filtered.split(",")[1]
price_float = float(price_filtered2)
# @ email sending
import smtplib
import ssl
from email.message import EmailMessage
email_sender = "youremail"
email_password = "yourpass"
email_reciever = "receivermail"
subject = "Hello well done"
body = f'''
Acer nitro 5 \nPrice: {price_float}'''
# email message
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)
contexts = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com' , 465, context=contexts) as smtp:
    smtp.login(user=email_sender, password=email_password)
    smtp.sendmail(email_sender,email_reciever, em.as_string())
