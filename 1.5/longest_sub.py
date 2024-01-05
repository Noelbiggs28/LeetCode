class Solution:
    def lengthOfLIS(self, nums):
        
        streaks = [1 for number in nums]
        for index in range(len(nums)-1):
            current_number = nums[index]
            for next_num in nums[index:]:
                if current_number < next_num:
                    streaks[index] +=1
                    current_number = next_num


        answer = max(streaks)
        return streaks