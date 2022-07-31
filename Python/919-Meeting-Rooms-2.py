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
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here

        startTimes = []
        endTimes = []

        for i in intervals:
            startTimes.append(i.start)
            endTimes.append(i.end)

        startTimes.sort()
        endTimes.sort()
        rooms = 0
        s, e, max_rooms = 0, 0, 0

        while s < len(startTimes):
            if startTimes[s] < endTimes[e]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                s += 1

            elif startTimes[s] >= endTimes[e]:
                rooms -= 1
                e += 1

        return max_rooms


        # TC: O(n log n)