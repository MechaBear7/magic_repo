"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-17 14:19:14
LastEditors: Helei.Yang
LastEditTime: 2025-01-17 14:23:07
FilePath: /magic_repo/leetcode/57.insert-interval_20250117.py
Description: 
"""

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
        intervals.append(newInterval)
        intervals.sort()
        def merge(intervals):
            result = []
            left, right = intervals[0]
            for i in range(1, len(intervals)):
                if intervals[i][0] <= right:
                    right = max(right, intervals[i][1])
                else:
                    result.append([left, right])
                    left, right = intervals[i]
            result.append([left, right])
            return result
        return merge(intervals)

# @lc code=end



#
# @lcpr case=start
# [[1,3],[6,9]]\n[2,5]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,5],[6,7],[8,10],[12,16]]\n[4,8]\n
# @lcpr case=end

#

