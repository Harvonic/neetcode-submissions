"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # sort by start times
        intervals.sort(key=lambda x: x.start)

        prev = float('-inf')

        for i in intervals:
            if i.start < prev:
                return False
            prev = i.end
        
        return True
