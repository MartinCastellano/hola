import configparser
conf = configparser.ConfigParser()

conf['General']={'chrome':'/home/martin/Downloads/Practicas/seleniumTest/drivers/chromedriver'}

conf['Paginas']={'page':'https://www.google.com'}

with open('conf.ini','w') as archivoconf:
    conf.write(archivoconf)