import time
import random
import multiprocessing
from threading import Thread
from counter.multiprocess_counter import MultiprocessCounter
from counter.threaded_counter import ThreadedCounter

def create_shared_counter_state(manager, min_value=None, max_value=None):
    """Create shared state for multiprocess counter."""
    return {
        'value': manager.dict(),
        'stats': manager.dict(),
        'lock': manager.Lock(),
        'min_value': min_value,
        'max_value': max_value
    }

def mp_counter_worker(shared_state, worker_id):
    counter = MultiprocessCounter(
        shared_state['value'],
        shared_state['stats'],
        shared_state['lock'],
        shared_state['min_value'],
        shared_state['max_value']
    )
    for _ in range(50):
        op = random.random()
        if op < 0.4:  # 40% increment
            try:
                counter.increment()
                print(f'MP Worker {worker_id} incremented')
            except ValueError:
                print(f'MP Worker {worker_id} increment failed (bounds)')
        elif op < 0.8:  # 40% decrement
            try:
                counter.decrement()
                print(f'MP Worker {worker_id} decremented')
            except ValueError:
                print(f'MP Worker {worker_id} decrement failed (bounds)')
        else:  # 20% read
            value = counter.get_value()
            print(f'MP Worker {worker_id} read value: {value}')
        time.sleep(0.05)

def thread_counter_worker(counter, worker_id):
    for _ in range(50):
        op = random.random()
        if op < 0.4:  # 40% increment
            try:
                counter.increment()
                print(f'Thread {worker_id} incremented')
            except ValueError:
                print(f'Thread {worker_id} increment failed (bounds)')
        elif op < 0.8:  # 40% decrement
            try:
                counter.decrement()
                print(f'Thread {worker_id} decremented')
            except ValueError:
                print(f'Thread {worker_id} decrement failed (bounds)')
        else:  # 20% read
            value = counter.get_value()
            print(f'Thread {worker_id} read value: {value}')
        time.sleep(0.05)

def test_counter():
    print("\n=== Testing Counter Implementations ===")
    
    # Test MultiprocessCounter - NOW with proper shared state!
    print("\nTesting MultiprocessCounter...")
    
    # Create shared state like the bank does
    manager = multiprocessing.Manager()
    shared_state = create_shared_counter_state(manager, min_value=-20, max_value=20)
    
    processes = [multiprocessing.Process(target=mp_counter_worker, args=(shared_state, i)) for i in range(3)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    
    # Now we can get meaningful final stats from shared state
    final_counter = MultiprocessCounter(
        shared_state['value'],
        shared_state['stats'],
        shared_state['lock'],
        shared_state['min_value'],
        shared_state['max_value']
    )
    print('MultiprocessCounter final value:', final_counter.get_value())
    print('MultiprocessCounter final stats:', final_counter.get_stats())
    
    # Test ThreadedCounter
    print("\nTesting ThreadedCounter...")
    threaded_counter = ThreadedCounter(min_value=-20, max_value=20)
    
    threads = [Thread(target=thread_counter_worker, args=(threaded_counter, i)) for i in range(3)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print('ThreadedCounter final value:', threaded_counter.get_value())
    print('ThreadedCounter final stats:', threaded_counter.get_stats())

if __name__ == '__main__':
    test_counter() 