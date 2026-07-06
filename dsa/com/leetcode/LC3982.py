class Main: 
    

    def digitRange(num) -> int:
        arr = [int(d) for d in str(num)]
        return max(arr) - min(arr)


    def maxDigitRange(nums: list[int]) -> int:
        ans = 0
        maxDigiRange = -1
        digiRanges = []

        for num in nums:

            digiRange = Main.digitRange(num)
            if digiRange > maxDigiRange:
                maxDigiRange = digiRange
            digiRanges.append((num, digiRange))

        # print(digiRanges)
        # print(maxDigiRange)

        for k,v in digiRanges:
            if v == maxDigiRange:
                print(k)
                ans += k

        return ans


    def main():
        # nums = [123, 456, 789]
        nums = [76364,80946,83426,86822,8470,77400,91853,17447,37800,96545,84619,58374,35177,32777,97032,59483,19578,5770,90000,65561,11209,66371,24953,4463,11437,45951,55753,96286,37364,30585,40914,74370,78195,84824,3592,97757,11186,22197,77593,96587,73024,12818,18252,48610,90339,97032,5513,6493]
        result = Main.maxDigitRange(nums)
        return result