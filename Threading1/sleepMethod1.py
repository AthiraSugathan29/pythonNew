# Single Threading
from time import sleep
def task():
    sleep(2) # Block the process for a moment
    print("This is from another thread") #Then display this message

#task()

from threading import Thread
threadObj = Thread(target=task)
threadObj.start()