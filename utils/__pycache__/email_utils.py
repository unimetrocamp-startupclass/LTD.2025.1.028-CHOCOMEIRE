import smtplib
from email.message import EmailMessage

def enviar_email(destinatario, assunto, corpo, anexo):
    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = 'seuemail@seudominio.com'
    msg['To'] = destinatario
    msg.set_content(corpo)

    with open(anexo, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=anexo)

    with smtplib.SMTP_SSL('smtp.seuprovedor.com', 465) as smtp:
        smtp.login('seuemail@seudominio.com', 'sua_senha')
        smtp.send_message(msg)