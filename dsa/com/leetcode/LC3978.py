class Main: 
    
    def isMiddleElementUnique(nums: list[int]) -> int:

        middleIdx = int((len(nums)-1)/2)
        middleIdxCnt = 0

        for num in nums:
            if nums[middleIdx] == num:
                middleIdxCnt += 1

        return middleIdxCnt == 1


    def main():
        nums = [1,2,3]
    
        result = Main.isMiddleElementUnique(nums)
        return result