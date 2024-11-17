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
        def backtracking(result, path, nums, pick_num, start_idx):
            if pick_num == 0:
                result.append(path[:])
                return
            if start_idx >= len(nums):
                return
            path.append(nums[start_idx])
            backtracking(result, path, nums, pick_num - 1, start_idx + 1)
            path.pop()
            backtracking(result, path, nums, pick_num, start_idx + 1)

        result = []
        for pick_num in range(0, len(nums) + 1):
            backtracking(result, [], nums, pick_num, 0)
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
