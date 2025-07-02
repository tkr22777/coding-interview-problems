import time
import random
import multiprocessing
from threading import Thread
from bounded_queue.multiprocess_queue import MultiprocessQueue
from bounded_queue.threaded_queue import ThreadedQueue

def create_shared_queue_state(manager, max_size=100):
    """Create shared state for multiprocess queue."""
    lock = manager.Lock()
    return {
        'data': manager.list(),
        'stats': manager.dict(),
        'lock': lock,
        'conditions': {
            'not_full': manager.Condition(lock),
            'not_empty': manager.Condition(lock)
        },
        'max_size': max_size
    }

def mp_producer(shared_state, producer_id):
    queue = MultiprocessQueue(
        shared_state['data'],
        shared_state['stats'],
        shared_state['lock'],
        shared_state['conditions'],
        shared_state['max_size']
    )
    for i in range(20):
        item = f'item_{producer_id}_{i}'
        if queue.put(item, timeout=1.0):
            print(f'MP Producer {producer_id} added {item}')
        time.sleep(random.random() * 0.2)

def mp_consumer(shared_state, consumer_id):
    queue = MultiprocessQueue(
        shared_state['data'],
        shared_state['stats'],
        shared_state['lock'],
        shared_state['conditions'],
        shared_state['max_size']
    )
    for i in range(20):
        item = queue.get(timeout=1.0)
        if item:
            print(f'MP Consumer {consumer_id} got {item}')
        time.sleep(random.random() * 0.3)

def thread_producer(queue, producer_id):
    for i in range(20):
        item = f'item_{producer_id}_{i}'
        if queue.put(item, timeout=1.0):
            print(f'Thread Producer {producer_id} added {item}')
        time.sleep(random.random() * 0.2)

def thread_consumer(queue, consumer_id):
    for i in range(20):
        item = queue.get(timeout=1.0)
        if item:
            print(f'Thread Consumer {consumer_id} got {item}')
        time.sleep(random.random() * 0.3)

def test_queue():
    print("\n=== Testing Queue Implementations ===")
    
    # Test MultiprocessQueue - NOW with proper shared state!
    print("\nTesting MultiprocessQueue...")
    
    # Create shared state like the bank does
    manager = multiprocessing.Manager()
    shared_state = create_shared_queue_state(manager, max_size=5)
    
    producers = [multiprocessing.Process(target=mp_producer, args=(shared_state, i)) for i in range(2)]
    consumers = [multiprocessing.Process(target=mp_consumer, args=(shared_state, i)) for i in range(2)]
    
    [p.start() for p in producers + consumers]
    [p.join() for p in producers + consumers]
    
    # Now we can get meaningful final stats from shared state
    final_queue = MultiprocessQueue(
        shared_state['data'],
        shared_state['stats'],
        shared_state['lock'],
        shared_state['conditions'],
        shared_state['max_size']
    )
    print('MultiprocessQueue final stats:', final_queue.get_stats())
    
    # Test ThreadedQueue
    print("\nTesting ThreadedQueue...")
    threaded_queue = ThreadedQueue(max_size=5)
    
    producers = [Thread(target=thread_producer, args=(threaded_queue, i)) for i in range(2)]
    consumers = [Thread(target=thread_consumer, args=(threaded_queue, i)) for i in range(2)]
    
    [p.start() for p in producers + consumers]
    [p.join() for p in producers + consumers]
    print('ThreadedQueue final stats:', threaded_queue.get_stats())

if __name__ == '__main__':
    test_queue() 