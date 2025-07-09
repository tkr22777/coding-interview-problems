import unittest
import threading
import time
from collections import defaultdict
from typing import Dict
from threading import Lock
from sortedcontainers import SortedDict
import heapq

class TransactionAggregator:

    def __init__(self) -> None:
        self.__users_balance: Dict[str, int] = defaultdict(int)
        self.locks: Dict[str, Lock] = defaultdict(Lock)
        self.ordered_events: Dict[str, SortedDict] = defaultdict(lambda: SortedDict({}))

    def record_event(self, account_id: str, amount: int, timestamp: int) -> None:
        with self.locks[account_id]:
            self.__users_balance[account_id] += amount

            if account_id not in self.ordered_events:
                self.ordered_events[account_id] = SortedDict()
            
            if timestamp not in self.ordered_events[account_id]:
                self.ordered_events[account_id][timestamp] = 0

            # summing since multiple records may have the same ts 
            self.ordered_events[account_id][timestamp] += amount
        
    def get_balance(self, account_id: str) -> int:
        return self.__users_balance[account_id]
    
    def get_flow(self, account_id: str, ts_start: int, ts_end: int) -> int:
        with self.locks[account_id]:
            if account_id in self.ordered_events:
                keys = self.ordered_events[account_id].irange(ts_start, ts_end)
                flow_amt = 0
                for key in keys:
                    flow_amt += self.ordered_events[account_id][key]
                return flow_amt
    
    def top_accounts(self, n: int, window_secs: int):
        ts_now = int(time.time())

        heap = []
        for account_id, orderd_events in self.ordered_events.items():
            total = self.get_flow(account_id, ts_now - window_secs, ts_now)
            heapq.heappush(heap, (total, account_id))
            if len(heap) > n:
                heapq.heappop(heap)
        
        accounts = []

        for total, account_id in heap:
            accounts.append((account_id, total))
            
        return accounts

class TestTransactionAggregator(unittest.TestCase):
    def test_basic_balance_and_flow(self):
        agg = TransactionAggregator()
        ts = int(time.time())
        agg.record_event("A",  75, ts)
        agg.record_event("A", -25, ts+1)
        self.assertEqual(agg.get_balance("A"), 50)
        self.assertEqual(agg.get_flow(ts, ts+60), 50)

    def test_top_accounts(self):
        agg = TransactionAggregator()
        base = int(time.time())
        for i in range(5):
            agg.record_event("X", 10, base+i)
            agg.record_event("Y", 5,  base+i)
        top = agg.top_accounts(1, 60)
        self.assertEqual(top, [("X", 50)])

    def test_thread_safety(self):
        agg = TransactionAggregator()
        base = int(time.time())
        def worker():
            for _ in range(1000):
                agg.record_event("Z", 1, base)
        threads = [threading.Thread(target=worker) for _ in range(10)]
        for t in threads: t.start()
        for t in threads: t.join()
        self.assertEqual(agg.get_balance("Z"), 10_000)

if __name__ == "__main__":
    unittest.main()
    ta = TransactionAggregator()

    ta.record_event("tkr22777", 400, 1)
    ta.record_event("tkr22777", 100, 2)
    ta.record_event("tkr22777", 200, 2)
    ta.record_event("tkr22777", 300, 4)

    print(ta.get_balance(account_id="tkr22777"))
    print(ta.get_flow(account_id="tkr22777", ts_start=2, ts_end=3))
    print(ta.get_flow(account_id="tkr22777", ts_start=2, ts_end=4))
    print(ta.get_flow(account_id="tkr22777", ts_start=0, ts_end=4))

    print(ta.top_accounts(2, 5))
