#
# @lc app=leetcode.cn id=78 lang=python3
# @lcpr version=30204
#
# [78] 子集
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(result, path, nums, idx, k):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtracking(result, path, nums, i + 1, k)
                path.pop()

        result = []
        for k in range(len(nums) + 1):
            backtracking(result, [], nums, 0, k)
        return result


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
