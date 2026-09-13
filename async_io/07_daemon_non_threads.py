# Daemon Therads are those threds which will stop 
# the thread when main thread finishes
# the executions where as non daemon threads are not

import threading, time
def load_images():
    while True:
        print("Image Loaded ...")
        time.sleep(3)
# Daemon is on
threading.Thread(target=load_images, daemon=True).start()
# Daemon is off
# threading.Thread(target=load_images).start()
print("This is main thread")
    