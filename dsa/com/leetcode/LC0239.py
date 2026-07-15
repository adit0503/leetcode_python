from typing import List


class Main:

    def maxSlidingWindow0(nums: List[int], k: int) -> List[int]:
        ans = []
        i, j = 0, len(nums)

        while(i+k <= j):
            ans.append(max(nums[i:i+k]))
            i += 1

        return ans
    

    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        ans = []
        i, j = 0, len(nums)
        mx = -100000

        while(i<j):
            if i==k:
                ans.append(mx)
            i += 1
    

    def main():
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3

        result = Main.maxSlidingWindow(nums, k)
        return result