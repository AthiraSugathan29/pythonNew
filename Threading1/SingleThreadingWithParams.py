# Single Threading with Parameters

from time import sleep
def task(sleep_time,msg):
    sleep(sleep_time)
    print(msg)

from threading import Thread
threadObj = Thread(target=task,args=(2,'This is another Thread'))
threadObj.start()
print("Waiting for the thread")
threadObj.join()