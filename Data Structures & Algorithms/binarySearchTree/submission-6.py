class TreeMap:
    
    def __init__(self):
        self.map = {}


    def insert(self, key: int, val: int) -> None:
        self.map[key] = val


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        return self.map[key]


    def getMin(self) -> int:
        if not self.map:
            return -1
        list_keys = self.map.keys()
        return self.map[min(list_keys)]


    def getMax(self) -> int:
        if not self.map:
            return -1
        list_keys = self.map.keys()
        return self.map[max(list_keys)]


    def remove(self, key: int) -> None:
        self.map.pop(key, None)


    def getInorderKeys(self) -> List[int]:
        list_keys = self.map.keys()
        return sorted(list_keys)
