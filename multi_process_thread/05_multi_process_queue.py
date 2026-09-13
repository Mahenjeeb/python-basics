from multiprocessing import Process, Queue, Value
import time

# def powAndAdd(num, queue):
#     res = num ** 5
#     queue.put(res)
# if __name__ == '__main__':
#     queue = Queue()
#     process = [Process(target=powAndAdd, args=(10, queue)) for _ in range(3)]
#     start = time.time()
#     [task.start() for task in process]
#     [task.join() for task in process]
#     end = time.time()
#     print(f"Time Taken {end - start:.2f} seconds")
#     while not queue.empty():
#         print(f"Queue Results:{queue.get()}")
        
def powAndAdd(num,count):
    for i in range(3):
        count.value = num ** 7
if __name__ == '__main__':
    count = Value('i', 0)
    process = [Process(target=powAndAdd, args=(10, count)) for _ in range(3)]
    start = time.time()
    [task.start() for task in process]
    [task.join() for task in process]
    end = time.time()
    print(f"Time Taken {end - start:.2f} seconds")
    print(f"Value Results:{count.value}")