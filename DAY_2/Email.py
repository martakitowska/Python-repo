import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def wyslij_mail(subject, content, recipient):
    user = sender = "pythonintel@int.pl"
    password = "isapython;2025"
    host = "poczta.int.pl"
    port = 465

    mail = MIMEMultipart()
    mail["Subject"] = '[Trener] ' + subject
    mail["To"] = recipient
    mail["From"] = sender

    body = MIMEText(content)
    mail.attach(body)

    with smtplib.SMTP_SSL(host, port) as serwer:
       serwer.login(user, password)
       serwer.send_message(mail)

    print("Wysłano mail!")

wyslij_mail('TEMAT', 'TREŚĆ', 'python@niepodam.pl')