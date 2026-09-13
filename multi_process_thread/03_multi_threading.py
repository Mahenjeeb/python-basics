import threading, time

pizza_list_01 = ['Buy Dough', 'Roll Dough', 'Bake']
pizza_list_02 = ['Wash Lettuce', 'Cut Tomatoes', 'Mix']
# Lock is use to 
lock = threading.Lock()
start = time.time()

shared_list = []
def buy_items(items, thread_id):
    for item in enumerate(items, start=1):
        with lock:
            shared_list.append(item)
            time.sleep(0.1)
            print(f"Thread {thread_id}: Added {item}. List is now: {shared_list}")

thread1 = threading.Thread(target=buy_items, args=(pizza_list_01, 1), name="Pizza-Worker-01")
thread2 = threading.Thread(target=buy_items, args=(pizza_list_02, 2), name="Pizza-Worker-02")

thread1.start()
thread2.start()
thread1.join()
thread2.join()
thread1.is_alive()
thread2.is_alive()
end = time.time()
print(f"Total Time Taken By Threads is {(end - start):.2f}")