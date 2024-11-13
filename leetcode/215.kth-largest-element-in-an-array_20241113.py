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
            # 随机选择基准数
            pivot = random.choice(nums)
            small, equal, big = [], [], []
            for i in range(len(nums)):
                if nums[i] == pivot:
                    equal.append(nums[i])
                elif nums[i] < pivot:
                    small.append(nums[i])
                else:
                    big.append(nums[i])
            if k <= len(big):
                return quick_select(big, k)
            elif len(nums) - len(small) < k:
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
