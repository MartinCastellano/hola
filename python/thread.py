import threading
import time



def fun():
    print('ran')
    time.sleep(1)
    print('donde')


# x = threading.Thread(target=fun)
# x.start()

print(threading.activeCount())

def count(n):
    for i in range(1,n+1):
        print(i)
        time.sleep(0.01)

for _ in range(2):
    x = threading.Thread(target=count,args=(10,))
    x.start()

x.join() #espera hasta q se termine el hilo
print('done')    