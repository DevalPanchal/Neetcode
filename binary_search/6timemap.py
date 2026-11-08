'''
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
'''


class TimeMap:

    def __init__(self):
        self.tmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmap:
            self.tmap[key] = []
        self.tmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.tmap[key] if key in self.tmap else []
        result = ""
        low = 0
        high = len(values) - 1

        while low <= high:
            mid = (low + high) // 2

            if values[mid][0] <= timestamp:
                result = values[mid][1]
                low = mid + 1
            else:
                high = mid - 1

        return result

    def printTimeMap(self):
        print(self.tmap)


timeMap = TimeMap()
timeMap.set("alice", "happy", 1)
timeMap.set("alice", "happy", 1);  
timeMap.get("alice", 1);           
timeMap.get("alice", 2);           
timeMap.set("alice", "sad", 3);    
timeMap.get("alice", 3);  

timeMap.printTimeMap()

