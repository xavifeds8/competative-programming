class LRU:
    def __init__(self , size) -> None:
        self.size = size
        self.cache = []
        self.d = {}

    def cacheit(self , key):
        if key in self.cache:
            self.cache.remove(key)
            self.cache.append(key)
        else:
            self.cache.pop(0)
            self.cache.append(key)
        

    def set(self , key , value):
        if len(self.d) > self.size:
            self.d.pop(self.cache.pop(0))
            self.d[key]  = value
        else:
            self.d[key] = value
        self.cacheit(key)
    
    def get(self , key):
        self.cacheit(key)
        return self.d[key]



