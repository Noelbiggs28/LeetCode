class Solution:
    def findMatrix(self, nums):
        num_count = {}
        for number in nums:
            if number in num_count:
                num_count[number]+=1
            else:
                num_count[number] = 1
        max_count = max(num_count.values())
        answer = []
        for round in range(max_count):
            inner_list = []
            for index in num_count:
                if num_count[index] !=0:
                    inner_list.append(index)
                    num_count[index] -=1
            answer.append(inner_list)
        return answer
    