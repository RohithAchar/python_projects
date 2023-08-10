from email.message import EmailMessage
import ssl
import smtplib

sender = 'rohithachar2000@gmail.com'
password = 'ssdfzfvvlnwbtczp'

reciever = ['ankithachar2000@gmail.com','ranjithachar42@gmail.com']

sub = 'Ankith the bot'
content = """
Hello Iam under the wanter please help me!
"""
for i in range(len(reciever)) :
    em = EmailMessage()
    em['From'] = sender
    em['to'] = reciever[i]
    em['subject'] = sub
    em.set_content = content

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as sm:
        sm.login(sender,password)
        sm.sendmail(sender,reciever[i],em.as_string())



