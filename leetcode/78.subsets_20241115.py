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
        def backtracking(result, path, num_pick, start_idx):
            if num_pick == 0:
                result.append(path[:])
                return
            if start_idx + num_pick > len(nums):
                return
            for idx in range(start_idx, len(nums)):
                path.append(nums[idx])  # 选择当前数
                backtracking(result, path, num_pick - 1, idx + 1)
                path.pop()  # 不选择当前数

        result = [[]]
        for num_pick in range(1, len(nums) + 1):
            backtracking(result, [], num_pick, 0)
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
