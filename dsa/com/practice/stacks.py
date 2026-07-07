class Stacks:

    def learnStacks(nums):
        print(nums)

        nums.append(5)
        print(nums)

        peek = nums[-1]
        print(peek)

        nums.pop()
        print(nums)

    def main():
        nums = [1,2,3,4]
        Stacks.learnStacks(nums)
