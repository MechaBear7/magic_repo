"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-20 18:07:56
LastEditors: Helei.Yang
LastEditTime: 2025-01-20 18:09:29
FilePath: /magic_repo/leetcode/LCR 121.寻找目标值-二维数组_20250120.py
Description: 
"""

#
# @lc app=leetcode.cn id=LCR 121 lang=python3
# @lcpr version=30204
#
# [LCR 121] 寻找目标值 - 二维数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findTargetIn2DPlants(self, plants: List[List[int]], target: int) -> bool:
        if len(plants) == 0:
            return False
        idx, jdx = 0, len(plants[0]) - 1
        while idx < len(plants) and jdx >= 0:
            if plants[idx][jdx] == target:
                return True
            elif plants[idx][jdx] < target:
                idx += 1
            else:
                jdx -= 1
        return False

# @lc code=end



#
# @lcpr case=start
# [[2,3,6,8],[4,5,8,9],[5,9,10,12]]\n8\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5],[2,5,7]]\n4\n
# @lcpr case=end

#

