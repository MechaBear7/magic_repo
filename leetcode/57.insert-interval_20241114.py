#
# @lc app=leetcode.cn id=57 lang=python3
# @lcpr version=30204
#
# [57] 插入区间
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        def merge(intervals):
            start, end = intervals[0]
            for i in range(1, len(intervals)):
                if intervals[i][0] > end:
                    result.append([start, end])
                    start, end = intervals[i]
                else:
                    end = max(end, intervals[i][1])
            result.append([start, end])

        intervals.append(newInterval)
        intervals.sort()

        merge(intervals)

        return result


# @lc code=end


#
# @lcpr case=start
# [[1,3],[6,9]]\n[2,5]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,5],[6,7],[8,10],[12,16]]\n[4,8]\n
# @lcpr case=end

#
