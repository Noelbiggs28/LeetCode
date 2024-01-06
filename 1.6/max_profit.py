class Solution:
    def jobScheduling(self, startTime, endTime, profit):

        jobs = []
        for index in range(len(startTime)):
            job = (startTime[index], endTime[index], profit[index])
            jobs.append(job)
        max_profit = 0
        for job in jobs:
            print(job)
        return max_profit