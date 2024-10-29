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
        result = 0
        left, right = 0, len(height) - 1
        pre_max, suf_max = -float("inf"), -float("inf")
        while left < right:
            pre_cur, suf_cur = height[left], height[right]
            result += max(pre_max - pre_cur, 0)
            result += max(suf_max - suf_cur, 0)
            pre_max = max(pre_max, pre_cur)
            suf_max = max(suf_max, suf_cur)
            if pre_cur < suf_cur:
                left += 1
            else:
                right -= 1
        return result


# @lc code=end


#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#
