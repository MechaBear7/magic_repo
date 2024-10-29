#
# @lc app=leetcode.cn id=27 lang=python3
# @lcpr version=30204
#
# [27] 移除元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        input_idx = 0
        for search_idx in range(len(nums)):
            if nums[search_idx] == val:
                continue
            nums[input_idx] = nums[search_idx]
            input_idx += 1
        return input_idx
# @lc code=end



#
# @lcpr case=start
# [3,2,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2,3,0,4,2]\n2\n
# @lcpr case=end

#

