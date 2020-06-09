from twilio.rest import Client
import time

acc = ''

pasw = ''


twilioCli=Client(acc,pasw)
print('ingrese el destinatario')

destino='+54'+raw_input()
# destino= '+543515171127'
print('ingrese el mensaje')
mensaje =raw_input()

mensajito= twilioCli.messages.create(body='\n'+mensaje,from_='+12052559377',to=destino)


    







