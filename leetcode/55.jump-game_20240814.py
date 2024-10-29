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
        if len(nums) <= 1:
            return True
        max_pos = 0
        for idx in range(len(nums) - 1):
            if max_pos >= idx:  # 如果当前位置可达
                max_pos = max(max_pos, idx + nums[idx])
                if max_pos >= len(nums) - 1:
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

