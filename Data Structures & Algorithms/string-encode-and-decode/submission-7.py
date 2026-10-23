class Solution:

    # this funciton takes a list of strings and 
    # returns that list into one string 

    # input = ["test case", "hello"]
    # output = "#9test case#5hello"

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res, sizes = [], []

        for s in strs:
            sizes.append(len(s))

        # 9,5
        for size in sizes:
            res.append(str(size))
            res.append(',')
        
        # 9,5#test casehello
        res.append('#')
        res.extend(strs)
        
        return ''.join(res)

    # this function takes a string and returns a list of strings
    # input = "9,5#test casehello""
    # output = ["test case", "hello"]
    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res, sizes, i = [], [], 0
        length = ""

        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1

        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res

                



