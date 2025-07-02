import time
import random
import multiprocessing
from threading import Thread, Lock
from multiprocess_bank import MultiprocessBank
from threaded_bank import ThreadedBank
from bank_interface import InvalidUserException, UserExistsException, InsufficientFundsException

def mp_bank_worker(shared_state, worker_id):
    # Create bank instance with shared state
    bank = MultiprocessBank(
        shared_state['users'],
        shared_state['balances'],
        shared_state['user_locks'],
        shared_state['global_lock']
    )
    
    # Create a user for this worker
    user_id = f'test_user_{worker_id:08d}'
    try:
        bank.add_user(user_id)
        print(f'MP Worker {worker_id} created user {user_id}')
    except UserExistsException:
        print(f'MP Worker {worker_id}: user {user_id} already exists')
    
    # Run random operations
    for _ in range(20):
        op = random.random()
        if op < 0.3:  # 30% deposits
            amount = random.uniform(10, 100)
            try:
                bank.deposit(user_id, amount)
                print(f'MP Worker {worker_id} deposited ${amount:.2f} to {user_id}')
            except Exception as e:
                print(f'MP Worker {worker_id} deposit failed: {e}')
        elif op < 0.6:  # 30% withdrawals
            amount = random.uniform(5, 50)
            try:
                bank.withdraw(user_id, amount)
                print(f'MP Worker {worker_id} withdrew ${amount:.2f} from {user_id}')
            except Exception as e:
                print(f'MP Worker {worker_id} withdraw failed: {e}')
        else:  # 40% transfers
            # Try to transfer to another worker's user
            target_worker = random.randint(0, 4)
            target_user = f'test_user_{target_worker:08d}'
            amount = random.uniform(1, 20)
            try:
                bank.transfer(user_id, target_user, amount)
                print(f'MP Worker {worker_id} transferred ${amount:.2f} from {user_id} to {target_user}')
            except Exception as e:
                print(f'MP Worker {worker_id} transfer failed: {e}')
        
        time.sleep(0.1)

def thread_bank_worker(bank, worker_id):
    # Create a user for this worker
    user_id = f'test_user_{worker_id:08d}'
    try:
        bank.add_user(user_id)
        print(f'Thread {worker_id} created user {user_id}')
    except UserExistsException:
        print(f'Thread {worker_id}: user {user_id} already exists')
    
    # Run random operations
    for _ in range(20):
        op = random.random()
        if op < 0.3:  # 30% deposits
            amount = random.uniform(10, 100)
            try:
                bank.deposit(user_id, amount)
                print(f'Thread {worker_id} deposited ${amount:.2f} to {user_id}')
            except Exception as e:
                print(f'Thread {worker_id} deposit failed: {e}')
        elif op < 0.6:  # 30% withdrawals
            amount = random.uniform(5, 50)
            try:
                bank.withdraw(user_id, amount)
                print(f'Thread {worker_id} withdrew ${amount:.2f} from {user_id}')
            except Exception as e:
                print(f'Thread {worker_id} withdraw failed: {e}')
        else:  # 40% transfers
            # Try to transfer to another worker's user
            target_worker = random.randint(0, 4)
            target_user = f'test_user_{target_worker:08d}'
            amount = random.uniform(1, 20)
            try:
                bank.transfer(user_id, target_user, amount)
                print(f'Thread {worker_id} transferred ${amount:.2f} from {user_id} to {target_user}')
            except Exception as e:
                print(f'Thread {worker_id} transfer failed: {e}')
        
        time.sleep(0.1)

def test_bank():
    print("\n=== Testing Bank Implementations ===")
    
    # Test MultiprocessBank
    print("\nTesting MultiprocessBank...")
    
    # Create shared state for multiprocessing
    manager = multiprocessing.Manager()
    user_ids = [f'test_user_{i:08d}' for i in range(5)]
    shared_state = {
        'users': manager.dict(),
        'balances': manager.dict(),
        'user_locks': {uid: manager.Lock() for uid in user_ids},
        'global_lock': manager.Lock()
    }
    
    # Create and run processes
    processes = [multiprocessing.Process(target=mp_bank_worker, args=(shared_state, i)) for i in range(5)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    
    # Check final state
    mp_bank = MultiprocessBank(
        shared_state['users'],
        shared_state['balances'], 
        shared_state['user_locks'],
        shared_state['global_lock']
    )
    print('\nMultiprocessBank final state:')
    print(f'Users: {mp_bank.list_users()}')
    for user in mp_bank.list_users():
        balance = mp_bank.get_balance(user)
        print(f'{user}: ${balance:.2f}')
    
    # Test ThreadedBank
    print("\nTesting ThreadedBank...")
    threaded_bank = ThreadedBank()
    
    threads = [Thread(target=thread_bank_worker, args=(threaded_bank, i)) for i in range(5)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    
    print('\nThreadedBank final state:')
    print(f'Users: {threaded_bank.list_users()}')
    for user in threaded_bank.list_users():
        balance = threaded_bank.get_balance(user)
        print(f'{user}: ${balance:.2f}')

if __name__ == '__main__':
    test_bank() 