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
        left, right = 0, len(height) - 1
        max_cnt = 0
        left_max, right_max = -float("inf"), -float("inf")
        while left < right:
            left_col, right_col = height[left], height[right]
            max_cnt += max(left_max - left_col, 0)
            max_cnt += max(right_max - right_col, 0)
            left_max = max(left_max, left_col)
            right_max = max(right_max, right_col)

            if left_col < right_col:
                left += 1
            else:
                right -= 1
        return max_cnt


# @lc code=end


#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#
