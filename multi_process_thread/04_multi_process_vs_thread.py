from multiprocessing import Process
from threading import Thread
import time

def run_process(operation, threshold):
    result = 0
    for i in range(threshold):
        result += i * i
    print(f"{operation}: Finished! Result is {result}")

p1 = Process(target=run_process, args=("Heavy Calculation 01", 50500000), name="Process-01")
p2 = Process(target=run_process, args=("Heavy Calculation 02", 19500000), name="Process-02")

if __name__ == '__main__':
    start = time.time()
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    end = time.time()
    print(f"Total Time Take for Process to Finish is {end - start:.2f} seconds")
    # Time Taken 4.60 seconds

# t1 = Thread(target=run_process, args=("Heavy Calculation 01", 50500000), name="Thread-01")
# t2 = Thread(target=run_process, args=("Heavy Calculation 02", 19500000), name="Thread-02")
# start = time.time()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end = time.time()
# print(f"Total Time Take for Thread to Finish is {end - start:.2f} seconds")
# Time Taken 5.06 seconds