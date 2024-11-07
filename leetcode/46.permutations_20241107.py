#
# @lc app=leetcode.cn id=46 lang=python3
# @lcpr version=30204
#
# [46] 全排列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(result, path, nums, masks):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for idx, mask in enumerate(masks):
                if not mask:
                    path.append(nums[idx])
                    masks[idx] = True
                    backtracking(result, path, nums, masks)
                    path.pop()
                    masks[idx] = False

        result = []
        masks = [False for _ in range(len(nums))]
        backtracking(result, [], nums, masks)
        return result


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
