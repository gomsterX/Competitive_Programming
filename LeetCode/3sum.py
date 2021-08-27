class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        l = len(nums)
        for i in range(l - 2):
            if nums[0] > 0:
                break
                
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            x = nums[i]
            start = i+1
            end = l - 1
            
            while start < end:
                s = x + nums[start] + nums[end]
                if s == 0:
                    triplets.append([x, nums[start], nums[end]])
                
                if s <= 0:
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start+=1
                else:
                    end -= 1
                    while start < end and nums[end] == nums[end+1]:
                        end-=1

        return(triplets)
