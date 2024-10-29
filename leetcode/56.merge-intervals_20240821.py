#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30204
#
# [56] 合并区间
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals)
        min_num = intervals[0][0]
        max_num = intervals[0][1]
        n_intervals = len(intervals)
        for i in range(1, n_intervals):
            if intervals[i][0] <= max_num:
                max_num = max(max_num, intervals[i][1])
            else:
                res.append([min_num, max_num])
                min_num = intervals[i][0]
                max_num = intervals[i][1]
        res.append([min_num, max_num])
        return res


# @lc code=end


#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

#
