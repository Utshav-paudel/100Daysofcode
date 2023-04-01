#email sending
import smtplib
import ssl
from email.message import EmailMessage
email_sender = "youremail"
email_password = "yourpass"
email_reciever = "receivermail"
subject = "Hello well done"
body = f'''
Acer nitro 5 \nPrice: '''

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
