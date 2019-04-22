import smtplib
import ssl
import configparser
from email.message import EmailMessage

class MailServer():
    
    PORT = 0
    EMAIL = 0
    PASSWORD = 0
    SUBJECT = 0
    HOST = 0

    def __init__(self, *args, **kwargs):
        config = configparser.ConfigParser()
        config.read('mail_config.ini')

        self.PORT = config['DEFAULT']['PORT']
        self.SUBJECT = config['DEFAULT']['SUBJECT']
        self.EMAIL = config['DEFAULT']['EMAIL']
        self.PASSWORD = config['DEFAULT']['PASSWORD']
        self.HOST = config['DEFAULT']['HOST']

    
    def send_mail(self, message_body, recipient, subject = None):
        message = """%s\nRegards,\nFoodie Bot""" % (message_body)

        server = smtplib.SMTP(self.HOST, self.PORT)
        server.ehlo()
        server.starttls()
        server.login(self.EMAIL, self.PASSWORD)
        msg = EmailMessage()
        msg.set_content(message)
        msg['From'] = self.EMAIL
        msg['To'] = recipient

        if subject == None:
            subject = self.SUBJECT

        msg['Subject'] = subject

        server.send_message(msg)
        server.quit()

