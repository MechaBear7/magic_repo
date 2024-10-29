#
# @lc app=leetcode.cn id=55 lang=python3
# @lcpr version=30204
#
# [55] 跳跃游戏
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, right_almost = len(nums), 0
        for i in range(n):
            if i <= right_almost:  # 如果当前位置可达
                right_almost = max(right_almost, i+nums[i])  # 最大的可达位置
                if right_almost >= n - 1:
                    return True
        return False
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,0,4]\n
# @lcpr case=end

#

