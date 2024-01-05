class Solution:
    def numberOfBeams(self, bank):
        devices_in_row = []
        for row in bank:
            devices = row.count("1")
            if devices != 0:
                devices_in_row.append(devices)
        if len(devices_in_row)==0:
            return 0
        answer = 0
        for index in range(len(devices_in_row)-1):
            beams = devices_in_row[index]*devices_in_row[index+1]
            answer+=beams
        return answer