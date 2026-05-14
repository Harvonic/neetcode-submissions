class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        output = []

        # find all the ones whos finish times < start time of new one
        new = newInterval

        overlapStart = 0

        for i in range(len(intervals)):
            if intervals[i][1] < new[0]:
                output.append(intervals[i])
            else:
                overlapStart = i
                break

        overlapEnd = len(intervals)
        
        # find the overlaps
        for j in range(overlapStart, len(intervals)):
            if not (intervals[j][1] < new[0] or intervals[j][0] > new[1]):
                new[0] = min(new[0], intervals[j][0])
                new[1] = max(new[1], intervals[j][1])
            else:
                overlapEnd = j
                break
        
        output.append(new)
        
        # add the ones after it
        for i in range(overlapEnd, len(intervals)):
            if intervals[i][0] > new[1]:
                output.append(intervals[i])

        return output

        

        
