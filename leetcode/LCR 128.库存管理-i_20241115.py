#
# @lc app=leetcode.cn id=LCR 128 lang=python3
# @lcpr version=30204
#
# [LCR 128] 库存管理 I
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        left, right = 0, len(stock) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if stock[mid] < stock[right]:
                right = mid
            elif stock[mid] > stock[right]:
                left = mid + 1
            else:
                right -= 1
        return stock[left]


# @lc code=end


#
# @lcpr case=start
# [4,5,8,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [5,7,9,1,2]\n
# @lcpr case=end

#
