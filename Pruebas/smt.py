from email import message
from smtplib import SMTP
import smtplib
from decouple import config

mensaje = 'Hola Mundo'
subject = 'Prueba'

mensaje = 'Subject: {}\n\n{}'.format(subject, mensaje)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('', '')

server.sendmail('nubiacc79@gmail.com', 'ccrhdbj@outlook.com', mensaje)

server.quit()

print('Correo enviado con exito')