class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []

        intervals.sort(key=lambda x: x[0])
        
        current = intervals[0]
        for i in range(1, len(intervals)):
            if not (current[0] > intervals[i][1] or current[1] < intervals[i][0]):
                current = [min(current[0], intervals[i][0]), max(current[1], intervals[i][1])]
            else:
                res.append(current)
                current = intervals[i]
        res.append(current)
        return res

        