#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30204
#
# [42] 接雨水
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        max_result = 0
        pre_max, suf_max = 0, 0
        left, right = 0, len(height) - 1
        while left < right:
            max_result += max(pre_max - height[left], 0)
            max_result += max(suf_max - height[right], 0)
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_result


# @lc code=end


#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#
