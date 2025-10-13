class Bucket:
    def __init__(self):
        self.bucket = []
    
    def get(self, key):
        for (k,v) in (self.bucket):
            if k == key:
                return v
        return -1
    
    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key,value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]
