class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        end_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            start = i+1
            end = len(nums) - 1
            if(end_sum == target):
                break
            while(start < end):
                c_sum = nums[i] + nums[start] + nums[end]
                if abs(c_sum - target) < abs(end_sum - target):
                    end_sum = c_sum
                if c_sum > target:
                    end -= 1
                else:
                    start += 1

        return(end_sum)
