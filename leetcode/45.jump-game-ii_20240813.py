#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30204
#
# [45] 跳跃游戏 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_idx, end, step = 0, 0, 0
        for i in range(n - 1):
            if max_idx >= i:  # 当前位置可达
                max_idx = max(max_idx, i + nums[i])  # 更新最大可达位置
                if i == end:
                    step += 1
                    end = max_idx
        return step
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#

