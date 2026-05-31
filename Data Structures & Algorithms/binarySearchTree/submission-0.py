class TreeMap:
    
    def __init__(self):
        self.map = {}


    def insert(self, key: int, val: int) -> None:
        self.map[key] = val


    def get(self, key: int) -> int:
        if key in self.map:
            return self.map[key]
        else:
            return -1


    def getMin(self) -> int:
        if self.map:
            keys = self.map.keys()
            sortedKeys = sorted(keys)
            return self.map[sortedKeys[0]]
        else:
            return -1


    def getMax(self) -> int:
        if self.map:
            keys = self.map.keys()
            sortedKeys = sorted(keys)
            return self.map[sortedKeys[-1]]
        else:
            return -1


    def remove(self, key: int) -> None:
        self.map.pop(key, None)


    def getInorderKeys(self) -> List[int]:
        keys = self.map.keys()
        sortedKeys = sorted(keys)
        return sortedKeys
