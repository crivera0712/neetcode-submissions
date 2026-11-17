class TimeMap:
    # given a set of key value pairs, we are tasked with designing a ds
    # that can hold the same key for different time stamps
    # all of the timestamps for the set are strictly increasing 

    # init function creates an empty dict that takes a str as a key
    # and a list of tuples that contain a str and an int
    # O(1) space for this setup
    def __init__(self):
        self.track: dict[str, list[tuple[str,int]]] = {}

    # set function takes a key, value, and a timestamp as arguments
    # if a key is not already in our dict then init that key entry in the dict
    # append the given values to the key entry in the dict
    # this is O(m*n) space and O(1) time, m being the number of keys and n
    # being the value pair
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.track: 
            self.track[key] = []
        self.track[key].append((value, timestamp))

    # this function retrieves the given timestamp, if the timestamp cannot be 
    # found return the largest previous timestamp in the dict that is <= to the 
    # passed timestamp 
    # if no value is found it returns ""
    # O(1) space, O(logn) time comp
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
                
        
