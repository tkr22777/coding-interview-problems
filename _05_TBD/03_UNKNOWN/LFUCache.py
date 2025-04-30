# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

import random

class LFUCache(object):
    
    cap = 0
    time_counter = 0
    cache = {}
    usage = {}

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.time_counter = 0
        self.cache = {}
        self.usage = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:

            value = self.cache[key]

            self.time_counter += 1
            self.usage[key]["Count"] += 1
            self.usage[key]["Time"] = self.time_counter

            return value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.time_counter += 1

        
        if key in self.cache:
            self.cache[key] = value
            self.usage[key]["Count"] += 1
            self.usage[key]["Time"] = self.time_counter
        else:
            if self.cap is 0:
                return
            
            if len(self.cache) == self.cap:
                evictKey = self.findLeastUsedKey()
                print "Evict Key:" + str(evictKey)
                del self.cache[evictKey]
                del self.usage[evictKey]
            
            self.cache[key] = value
            
            if key not in self.usage:
                self.usage[key] = {}
                self.usage[key]["Count"] = 1
                self.usage[key]["Time"] = self.time_counter

    def findLeastUsedKey(self):

        key = None
        minValue = None
        timeCount = None
        
        for k in self.usage:
            kUsage = self.usage[k]
            if minValue is None:
                key = k
                minValue =  self.usage[k]["Count"]
                timeCount =  self.usage[k]["Time"]
	        elif minValue > self.usage[k]["Count"]:
                key = k
                minValue =  self.usage[k]["Count"]
                timeCount =  self.usage[k]["Time"]
 	        elif minValue == self.usage[k]["Count"] and timeCount < self.usage[k]["Time"]:	
                key = k
                minValue =  self.usage[k]["Count"]
                timeCount =  self.usage[k]["Time"]
        return key

