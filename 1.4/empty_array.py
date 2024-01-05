class Solution:
    def minOperations(self, nums):
        operations = 0
        unique_numbers = set(nums)
        amounts = {}
        for number in unique_numbers:
            amounts[number] = 0    
        for number in nums:
            amounts[number] += 1
        for number in amounts.keys():
            amount = amounts[number]
            if amount == 1:
                return -1
            if amount == 2:
                operations += 1
                continue
            if amount % 3 == 0:
                operations += amount / 3
            else:
                while amount % 3 !=0:
                    if amount == 0:         
                        break
                    amount = amount - 2
                    if amount == 1 or amount == -1:
                        return -1
                    operations +=1
                if amount != 0 and amount % 3 ==0:
                    operations += amount / 3
        return int(operations)