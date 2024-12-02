#
# @lc app=leetcode.cn id=912 lang=python3
# @lcpr version=30204
#
# [912] 排序数组
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(nums):
            if len(nums) == 0:
                return []
            pivot = random.choice(nums)
            small, equal, big = [], [], []
            for num in nums:
                if num < pivot:
                    small.append(num)
                elif num == pivot:
                    equal.append(num)
                else:
                    big.append(num)
            small = quick_sort(small)
            big = quick_sort(big)
            return small + equal + big

        return quick_sort(nums)


# @lc code=end


#
# @lcpr case=start
# [5,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,1,2,0,0]\n
# @lcpr case=end

#
