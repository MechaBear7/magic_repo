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
        max_pos = 0
        n = len(nums)
        for i in range(n - 1):
            if max_pos >= i:  # 当前位置可达
                max_pos = max(max_pos, i + nums[i])  # 更新最大可达位置
                if max_pos >= n - 1:
                    return True
            else:
                return False
        return max_pos >= n - 1


# @lc code=end


#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,0,4]\n
# @lcpr case=end

#
