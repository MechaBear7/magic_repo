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
        result = []
        intervals = sorted(intervals)
        min_num, max_num = intervals[0]
        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] <= max_num:
                max_num = max(max_num, intervals[i][1])
            else:
                result.append([min_num, max_num])
                min_num, max_num = intervals[i]
        result.append([min_num, max_num])
        return result


# @lc code=end


#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

#
