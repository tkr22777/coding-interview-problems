import time
import random
import multiprocessing
from threading import Thread
from resource_pool.multiprocess_pool import MultiprocessPool
from resource_pool.threaded_pool import ThreadedPool

def create_shared_pool_state(manager, resources=None, max_size=None):
    """Create shared state for multiprocess resource pool."""
    lock = manager.Lock()
    if resources is None:
        resources = []
    shared_resources = manager.list(resources)
    shared_available = manager.list(range(len(resources)))  # All resources initially available
    
    return {
        'resources': shared_resources,
        'available': shared_available,
        'stats': manager.dict(),
        'lock': lock,
        'condition': manager.Condition(lock),
        'max_size': max_size
    }

def mp_pool_worker(shared_state, worker_id):
    pool = MultiprocessPool(
        shared_state['resources'],
        shared_state['available'],
        shared_state['stats'],
        shared_state['lock'],
        shared_state['condition'],
        shared_state['max_size']
    )
    for _ in range(20):
        resource = pool.acquire(timeout=1.0)
        if resource is not None:
            print(f'MP Worker {worker_id} acquired {resource}')
            time.sleep(random.random() * 0.2)  # Simulate work
            if pool.release(resource):
                print(f'MP Worker {worker_id} released {resource}')
            else:
                print(f'MP Worker {worker_id} failed to release {resource}')
        else:
            print(f'MP Worker {worker_id} timed out')
        time.sleep(0.1)

def mp_context_worker(shared_state, worker_id):
    pool = MultiprocessPool(
        shared_state['resources'],
        shared_state['available'],
        shared_state['stats'],
        shared_state['lock'],
        shared_state['condition'],
        shared_state['max_size']
    )
    for _ in range(10):
        try:
            with pool.acquire_context(timeout=1.0) as resource:
                print(f'MP Context Worker {worker_id} acquired {resource}')
                time.sleep(random.random() * 0.2)
        except TimeoutError:
            print(f'MP Context Worker {worker_id} timed out')
        time.sleep(0.1)

def thread_pool_worker(pool, worker_id):
    for _ in range(20):
        resource = pool.acquire(timeout=1.0)
        if resource is not None:
            print(f'Thread {worker_id} acquired {resource}')
            time.sleep(random.random() * 0.2)
            if pool.release(resource):
                print(f'Thread {worker_id} released {resource}')
            else:
                print(f'Thread {worker_id} failed to release {resource}')
        else:
            print(f'Thread {worker_id} timed out')
        time.sleep(0.1)

def thread_context_worker(pool, worker_id):
    for _ in range(10):
        try:
            with pool.acquire_context(timeout=1.0) as resource:
                print(f'Thread Context Worker {worker_id} acquired {resource}')
                time.sleep(random.random() * 0.2)
        except TimeoutError:
            print(f'Thread Context Worker {worker_id} timed out')
        time.sleep(0.1)

def test_resource_pool():
    print("\n=== Testing Resource Pool Implementations ===")
    
    # Test MultiprocessPool - NOW with proper shared state!
    print("\nTesting MultiprocessPool...")
    
    # Create shared state like the bank does
    manager = multiprocessing.Manager()
    resources = ['resource_0', 'resource_1', 'resource_2']
    shared_state = create_shared_pool_state(manager, resources, max_size=5)
    
    # Test basic acquire/release
    processes = [multiprocessing.Process(target=mp_pool_worker, args=(shared_state, i)) for i in range(3)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    
    # Test context manager
    processes = [multiprocessing.Process(target=mp_context_worker, args=(shared_state, i)) for i in range(2)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    
    # Now we can get meaningful final stats from shared state
    final_pool = MultiprocessPool(
        shared_state['resources'],
        shared_state['available'],
        shared_state['stats'],
        shared_state['lock'],
        shared_state['condition'],
        shared_state['max_size']
    )
    print('MultiprocessPool final stats:', final_pool.get_stats())
    
    # Test ThreadedPool
    print("\nTesting ThreadedPool...")
    threaded_pool = ThreadedPool(max_size=5)
    
    # Add resources to the threaded pool
    for resource in resources:
        threaded_pool.add_resource(resource)
    
    # Test basic acquire/release
    threads = [Thread(target=thread_pool_worker, args=(threaded_pool, i)) for i in range(3)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    
    # Test context manager
    threads = [Thread(target=thread_context_worker, args=(threaded_pool, i)) for i in range(2)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    
    print('ThreadedPool final stats:', threaded_pool.get_stats())

if __name__ == '__main__':
    test_resource_pool() 