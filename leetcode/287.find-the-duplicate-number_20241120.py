#
# @lc app=leetcode.cn id=287 lang=python3
# @lcpr version=30204
#
# [287] 寻找重复数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        min_val = 1  # 所查找数字范围的最小值
        max_val = len(nums)  # 所查找数字范围的最大值

        while min_val < max_val:
            mid = (min_val + max_val) // 2
            # 计数
            cnt = sum(min_val <= num <= mid for num in nums)

            if cnt > mid - min_val + 1:  # 个数超出范围长度，即存在重复数
                max_val = mid
            else:
                min_val = mid + 1

        return min_val


# @lc code=end


#
# @lcpr case=start
# [1,3,4,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,3,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,3]\n
# @lcpr case=end

#
