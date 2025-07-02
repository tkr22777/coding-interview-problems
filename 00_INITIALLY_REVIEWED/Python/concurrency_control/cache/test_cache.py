import time
import random
import multiprocessing
from threading import Thread
from cache.multiprocess_cache import MultiprocessCache
from cache.threaded_cache import ThreadedCache

def create_shared_cache_state(manager, max_size=1000):
    """Create shared state for multiprocess cache."""
    return {
        'data': manager.dict(),
        'stats': manager.dict(),
        'lock': manager.Lock(),
        'max_size': max_size
    }

def mp_cache_worker(shared_state, worker_id):
    # Create cache instance with shared state - now truly shared!
    cache = MultiprocessCache(
        shared_state['data'],
        shared_state['stats'],
        shared_state['lock'],
        shared_state['max_size']
    )
    
    for _ in range(50):
        if random.random() > 0.7:  # 30% writes
            key = f'key_{random.randint(1,10)}'
            value = random.randint(1,1000)
            cache.put(key, value, ttl_seconds=2)
            print(f'MP Worker {worker_id} wrote {key}={value}')
        else:  # 70% reads
            key = f'key_{random.randint(1,10)}'
            value = cache.get(key)
            print(f'MP Worker {worker_id} read {key}={value}')
        time.sleep(0.1)

def thread_cache_worker(cache, worker_id):
    for _ in range(50):
        if random.random() > 0.7:  # 30% writes
            key = f'key_{random.randint(1,10)}'
            value = random.randint(1,1000)
            cache.put(key, value, ttl_seconds=2)
            print(f'Thread {worker_id} wrote {key}={value}')
        else:  # 70% reads
            key = f'key_{random.randint(1,10)}'
            value = cache.get(key)
            print(f'Thread {worker_id} read {key}={value}')
        time.sleep(0.1)

def test_cache():
    print("\n=== Testing Cache Implementations ===")
    
    # Test MultiprocessCache - NOW with proper shared state!
    print("\nTesting MultiprocessCache...")
    
    # Create shared state like the bank does
    manager = multiprocessing.Manager()
    shared_state = create_shared_cache_state(manager, max_size=5)
    
    processes = [multiprocessing.Process(target=mp_cache_worker, args=(shared_state, i)) for i in range(3)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    
    # Now we can get meaningful final stats from shared state
    final_cache = MultiprocessCache(
        shared_state['data'],
        shared_state['stats'],
        shared_state['lock'],
        shared_state['max_size']
    )
    print('MultiprocessCache final stats:', final_cache.get_stats())
    print('Final shared data keys:', list(shared_state['data'].keys()))
    
    # Test ThreadedCache - This DOES share properly
    print("\nTesting ThreadedCache...")
    threaded_cache = ThreadedCache(max_size=5)
    
    threads = [Thread(target=thread_cache_worker, args=(threaded_cache, i)) for i in range(3)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print('ThreadedCache final stats:', threaded_cache.get_stats())

if __name__ == '__main__':
    test_cache() 