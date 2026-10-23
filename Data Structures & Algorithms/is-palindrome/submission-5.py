class Solution:
    def isPalindrome(self, s: str) -> bool:

        # given a string s, return true if it is a palindrome
        # a palindrome is a string that reads the same forward as backward
        # input: racecar 
        # output: True 

        # constraints: same forward as backward, ignores all non-alphanumeric chars
        # alphanumeric chars consist of (a-z) and (0-9)

        if len(s) == 1:
            print("here")
            return True

        stripped = s.replace(" ", "").lower()

        left, right = 0, len(stripped) - 1

        # 0P
        while (left < right):

            if (not stripped[right].isalnum()):
                right -= 1
                continue

            if (not stripped[left].isalnum()):
                left += 1
                continue
            
            if (left > right):
                return True

            if stripped[left] != stripped[right]:
                return False

            left += 1 
            right -= 1

        return True

        