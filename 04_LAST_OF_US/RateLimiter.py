import time
from collections import defaultdict
from datetime import datetime, timedelta
from collections import OrderedDict

class RateLimiter:
    def __init__(self, max: int, window: int) -> None:
        self.max = max
        self.window = window

        # v1 specific
        # lets keep all requests for an user in an array in descending order:
        # e.g. u1 -> [13, 9, 7, 3, 1]
        # when a request with a timestamp t arrives, 
        # we binary search the index from 
        self.user_requests = defaultdict(list)
    
    def __str__(self) -> str:
        return "max:" + str(self.max) + " window:" + str(self.window)

    def allow_user_v1(self, user_id: str) -> bool:
        ur_list = self.user_requests[user_id]
        current_ts = datetime.now()
        window_start_ts = current_ts - timedelta(seconds=self.window)
        urs_in_window = list(filter(lambda x: x > window_start_ts, ur_list))

        # print("time:" + str(current_ts) + ", user requests list:" + str(ur_list))
        if len(urs_in_window) < self.max:
            urs_in_window.append(current_ts)
            self.user_requests[user_id] = urs_in_window
            # print("window start ts:" + str(window_start_ts) + ", user requests in window:" + str(len(urs_in_window)))
            return True
        else:
            self.user_requests[user_id] = urs_in_window
            # print("window start ts:" + str(window_start_ts) + ", user requests in window:" + str(len(urs_in_window)))
            return False
    
r = RateLimiter(2, 5)
print(r)
print(r.allow_user_v1("u1") == True)
print(r.allow_user_v1("u1") == True)
print(r.allow_user_v1("u1") == False)
print(r.allow_user_v1("u1") == False)
time.sleep(5)

print(r.allow_user_v1("u1") == True)

time.sleep(2)
print(r.allow_user_v1("u1") == True)
print(r.allow_user_v1("u1") == False)

time.sleep(3)
print(r.allow_user_v1("u1") == True)
print(r.allow_user_v1("u1") == False)
time.sleep(1)
print(r.allow_user_v1("u1") == False)
time.sleep(1)
print(r.allow_user_v1("u1") == True)

