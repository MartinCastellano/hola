#! python3
import  smtplib,time,datetime

smpo = smtplib.SMTP('smtp.gmail.com',587)
# smpo2 = smtplib.SMTP_SSL('smtp.gmail.com',465)


#hoy = datetime.datetime(2020,1,17,16,55,00)

smpo.ehlo() #hello message to the server 250
smpo.starttls() # encryption ready  220


smpo.login('martin.castellano89@gmail.com','')# logeado es necesario crear una contrasena de dispositivo 235

#hola=True
#while hola:
 #   if datetime.datetime.now() < hoy:  
smpo.sendmail(from_addr=' ',to_addrs='justocba@gmail.com',msg='Subject:soquetin\nholajusto ' )
  #      hola=False
print('mandado')
smpo.quit()# codigo 221
