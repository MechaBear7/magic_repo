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
        def backtracking(result, path, nums_pick, start_idx):
            if nums_pick == 0:
                result.append(path[:])
                return
            for i in range(start_idx, len(nums)):
                path.append(nums[i])
                backtracking(result, path, nums_pick - 1, i + 1)
                path.pop()

        result = []
        for i in range(len(nums) + 1):
            backtracking(result, [], i, 0)

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
