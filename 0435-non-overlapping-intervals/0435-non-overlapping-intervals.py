class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x:(x[1],x[0]))

        count = 1
        last_num = intervals[0][1]
        for i in range(len(intervals)):
            if(intervals[i][0]>=last_num):
                count += 1
                last_num = intervals[i][1]


        return len(intervals) - count 
