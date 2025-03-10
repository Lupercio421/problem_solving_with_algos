class TimeMap:

    def __init__(self):
        self.store = {} #key: list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        #binary search on values
        l,r = 0, len(values) - 1
        while l <= r:
            m = (l + r) //  2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                # can not assign the res as we are in invalid condition
                r = m - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Time complexity: O(logN) for get, O(1) for set