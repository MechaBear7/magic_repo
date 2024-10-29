#
# @lc app=leetcode.cn id=167 lang=python3
# @lcpr version=30204
#
# [167] 两数之和 II - 输入有序数组
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_idx, right_idx = 0, len(numbers) - 1
        while left_idx < right_idx:
            if numbers[left_idx] + numbers[right_idx] == target:
                return [left_idx + 1, right_idx + 1]
            elif numbers[left_idx] + numbers[right_idx] < target:
                left_idx += 1
            else:
                right_idx -= 1


# @lc code=end


#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n-1\n
# @lcpr case=end

#
