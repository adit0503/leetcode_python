class P4:

    def soln1(nums, w):
        ans = -100
        i, j = 0, len(nums)
        
        while(i+w <= j):
            ans = max(ans, max(nums[i:i+w]))
            # print(ans, i , i+w, nums[i:i+w])
            i += 1

        return ans


    def main():
        nums = [1,3,-1,-3,5,3,6,7]
        w = 3

        print("main ans: " + str(P4.soln1(nums, w)))
