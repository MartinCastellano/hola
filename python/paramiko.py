import paramiko,time,scp

from getpass import getpass

host = ''

user = 'martin'

if __name__ == "__main__":

    try:
        client = paramiko.SSHClient()

        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        password = getpass('ingrese pasword ')
        client.connect(host,username=user,password=password)

        scp_client = scp.SCPClient(client.get_transport())
        #mandamos un archivo a un path del servidor
        scp_client.put('localpath','remotepath')
        
        session = client.get_transport().open_session()#paara el calso q quiera otro usuario

        if session.active:


            session.set_combine_stderr(True)

            session.get_pty()

            session.exec_command('sudo ls -l')

            stdin = session.makefile('wb')#genero tunel

            stdout = session.makefile('rb')


            stdin.write(password + '\n')


            result = stdout.read().decode()

            print(result)


        
        
        
        client.close()
        #descargamos un archivo del servidor
        scp_client.get('path del servidor/archivo','donde lo quiero guardar')

        scp_client.close()#cerramos el cliente

        #aca pongo el codigo del comando q quiero q haga cuando me conecte al servidor
        stdin,stdout,stderr = client.exec_command('ls')
        time.sleep(1)

        result = stdout.read().decode()
        #mando un archivo al servidor
        sftp_client =client.open_sftp()

        sftp_client.put('README.md','servidor donde lo quiero mandar')

        sftp_client.close()
        #descargo un archivo q esta en e;l sevidor
        sftp_client.get('direccion y archivo del serviro ','donde lo quiero guardar')
        sftp_client.close()
        #una forma de hacer una salida por un canal seria (solo hace un comando y se cierra)
        session = client.get_transport().open_session()

        if session.active():

            session.exec_command('ls -l')

            result = session.recv(1024).decode()

            print(result)


        #luego hacemos una espera ,obtenemos la salidoa y la imprimo
        

        print(result)
    except paramiko.ssh_exception.AuthenticationException as e :

        print('pass incorrecta')


