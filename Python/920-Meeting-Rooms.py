from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here

        if not intervals: return True

        intervals.sort(key = lambda i: i.start)

        prevEnd = intervals[0].end

        for i in intervals[1:]:
            s = i.start
            e = i.end
            if s < prevEnd:
                return False

            else:
                prevEnd = e

        return True