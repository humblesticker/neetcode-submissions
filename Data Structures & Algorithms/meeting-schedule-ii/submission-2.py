class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)
        pq, rooms = [], 0

        for interval in intervals:
            # pq[0][0] minq end
            while pq and interval.start >= pq[0][0]: 
                heapq.heappop(pq)
            
            heapq.heappush(pq, (interval.end, interval.start))
            rooms = max(rooms, len(pq))

        return rooms        
"""
interval, pq, room
(0,40), [(40,0)], 1
(5,10), [(10,5), (40,0)], 2
(15,20), [(20,15),(40,0)], 2
"""