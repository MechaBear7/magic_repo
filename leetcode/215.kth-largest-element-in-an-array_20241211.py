#
# @lc app=leetcode.cn id=215 lang=python3
# @lcpr version=30204
#
# [215] 数组中的第K个最大元素
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            pivot = random.choice(nums)
            small, equal, big = [], [], []
            for num in nums:
                if num < pivot:
                    small.append(num)
                elif num == pivot:
                    equal.append(num)
                else:
                    big.append(num)
            if len(big) >= k:
                return quick_select(big, k)
            elif len(equal) + len(big) < k:
                return quick_select(small, k - len(equal) - len(big))
            else:
                return pivot

        return quick_select(nums, k)


# @lc code=end


#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#
