'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EmailUser
# The mail addresses and password
sender_address = EmailUser.MAIL_FROM
sender_pass = EmailUser.MAIL_FROM_PW
receiver_address = Email.MAIL_TO


def send_mail(mail_content, to_addr):
    subject = 'Trade condition alert! | cloud.trading.app'
    content = "Instructions:"+'\n'
    for order in mail_content:
        content += f"{order['side']} | {order['symbol']} | {order['coins']} tokens ({round(order['usd_amt'],2)} $)"+'\n'

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject
    # The body and the attachments for the mail
    message.attach(MIMEText(str(content), 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    # login with mail_id and password
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, to_addr, text)
    session.quit()
    print(
        f'mail sent! | from: {sender_address} | to: {to_addr} | subject: {subject} | content: {mail_content}|')
'''
