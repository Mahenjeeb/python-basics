import threading, time

pizza_list_01 = ['Buy Dough', 'Roll Dough', 'Bake']
pizza_list_02 = ['Wash Lettuce', 'Cut Tomatoes', 'Mix']

start = time.time()
def buy_items(items, delay):
    for index, item in enumerate(items, start=1):
        time.sleep(delay)
        print(f"{index} - {item}")

thread1 = threading.Thread(target=buy_items, args=(pizza_list_01, 0.1), name="Pizza-Worker-01")
thread2 = threading.Thread(target=buy_items, args=(pizza_list_02, 0.1), name="Pizza-Worker-02")
thread1.start()
thread2.start()
thread1.join()
thread2.join()
thread1.is_alive()
thread2.is_alive()
end = time.time()
print(f"Total Time Taken By Threads is {(end - start):.2f}")