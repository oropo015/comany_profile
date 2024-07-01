import smtplib, ssl, os


def email_sender(message_):
    port = 465
    host = "smtp.gmail.com"
    password = os.getenv("PASSWORD")
    email_ = "techternethub@gmail.com"
    receiver_ = "techternethub@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email_, password)
        server.sendmail(email_, receiver_, message_)