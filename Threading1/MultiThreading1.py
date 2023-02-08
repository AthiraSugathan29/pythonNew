import time
import threading

def cal_sqr(arrnum):
    print("Calculate the square of the number")
    for i in arrnum:
        time.sleep(0.3)
        print("Square : ",i*i)
def cal_cube(arrnum):
    print("Calculate the cube of the number")
    for i in arrnum:
        time.sleep(0.3)
        print("Cube : ",i*i*i)
arr = [1,2,3,4,5]
t1 = time.time()
# cal_sqr(arr) # Using Normal function call
# cal_cube(arr)

obj1 = threading.Thread(target=cal_sqr,args=(arr,))
obj2 = threading.Thread(target=cal_cube,args=(arr,))
obj1.start()
obj2.start()
obj1.join()
obj2.join()
print("Total time taken : ",time.time()-t1)
