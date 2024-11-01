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
        max_pos = 0
        jmp_cnt, jmp_end = 0, 0
        for i in range(len(nums) - 1):
            if max_pos >= i:  # 当前位置可达
                max_pos = max(max_pos, i + nums[i])
                if i == jmp_end:  # 跳跃 jmp_cnt 次数的最远可达位置
                    jmp_cnt += 1
                    jmp_end = max_pos
            else:
                return -1
        return jmp_cnt


# @lc code=end


#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#
