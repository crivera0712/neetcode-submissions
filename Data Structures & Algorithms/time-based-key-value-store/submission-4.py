class TimeMap:
    # {
    # [10,20,30]
    def __init__(self):
        self.track: dict[str, list[tuple[str,int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.track: 
            self.track[key] = []
        self.track[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        val = self.track.get(key,[])
        if len(val) < 1:
            return ""
        
        left = 0
        right = len(val) - 1

        while left <= right: 
            mid = (left + right) // 2
            if val[mid][1] == timestamp:
                return val[mid][0]
            if val[mid][1] < timestamp: 
                left = mid + 1
            else: 
                right = mid - 1
        
        if val[right][1] > timestamp:
            return ""
        return val[right][0]
                
        
