from threading import Thread
import time
def run_thread01():
    for i in range(1,4):
        time.sleep(1)
        print(f"I am running thread 01 {i}")
def run_thread02():
    for i in range(1,4):
        time.sleep(3)
        print(f"I am running thread 02 {i}")

one_thread = Thread(target=run_thread01, name='Worker-1')
one_thread.start()
two_thread = Thread(target=run_thread02, name='Worker-2')
two_thread.start()
two_thread.join()
one_thread.join()
