import smtplib
import ssl
from email.message import EmailMessage
from datetime import date
from cotacaoHTML import moeda, carteira

def send_email(message1, message2):
    hoje = str(date.today().strftime("%d/%m/%Y"))
    subject = "Cotações do dia: " + hoje
    body = message1 + message2
    sender_email = "youremail@gmail.com"
    receiver_email = "youremail@gmail.com"
    password = "password"

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    html = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p>
        </body>
    </html>
    """

    message.add_alternative(html, subtype="html")

    context = ssl.create_default_context()

    print("Sending Email!")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Success")

send_email(carteira(7), moeda())
