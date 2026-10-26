class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # we are given a list of integers where piles[i] is the number of bananas 
        # in the ith pile. We are also given an integer h, h is the numbers of hours
        # that we have to eat all the bananas
        
        # we must deicde on the bananas per hour to eat, eating rate of k
        # each hour we must choose a pile of bananas and eat k amount of bananas from 
        # that pile. if that pile has less than k bananas, we can finish eating from it
        # but we cannot eat from another pile in the same hour 
        # return the min integer k such that we can eat all of the bananas within k hours 

        # constraints: we must eat all the bananas within h hours
        # we cannot move onto another pile if k > piles[i] within the same hour
        # must return an integer k, there will always be an output 

        # input = [1,4,3,2] h = 9
        
        # sort the list and apply binary search 
        # sorted = [3,6,7,11] h = 8
        # 

        left, right = 1, max(piles)
        k = 0
        

        while left <= right:
            mid = (left + right) // 2
            time_to_eat = 0

            for pile in piles:
                time_to_eat += math.ceil(pile/mid)
            if time_to_eat <= h:
                k = mid
                right = mid - 1
            elif time_to_eat > h:
                left = mid + 1
        
        return k

        