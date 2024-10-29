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
        max_pos, end, step = 0, 0, 0
        n = len(nums)
        for i in range(n - 1):
            if max_pos >= i:  # 当前位置可达
                max_pos = max(max_pos, i + nums[i])
                if end == i:
                    end = max_pos
                    step += 1
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
