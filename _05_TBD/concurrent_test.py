import threading

counter = 0
num_increments = 100000
num_threads = 100
lock = threading.Lock()


def increment_counter():
    global counter
    with lock:
        for _ in range(num_increments):
            counter += 1
    # for _ in range(num_increments):
    #     counter += 1


threads = []


# Creating and starting threads
for i in range(num_threads):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

# Waiting for all threads to finish
for thread in threads:
    thread.join()

# Printing the final value of the counter
print(f"Final counter value: {counter}")