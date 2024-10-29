#
# @lc app=leetcode.cn id=724 lang=python3
# @lcpr version=30204
#
# [724] 寻找数组的中心下标
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l2r = [1 for _ in range(len(nums))]  # 记录 idx 左侧数的和
        r2l = [1 for _ in range(len(nums))]  # 记录 idx 右侧数的和

        for idx in range(len(nums)):
            if idx == 0:
                continue
            l2r[idx] = l2r[idx-1] + nums[idx-1]
        for idx in reversed(range(len(nums))):
            if idx == len(nums) - 1:
                continue
            r2l[idx] = r2l[idx+1] + nums[idx+1]
        
        for idx in range(len(nums)):
            if l2r[idx] == r2l[idx]:
                return idx
            
        return -1
# @lc code=end



#
# @lcpr case=start
# [1, 7, 3, 6, 5, 6]\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 3]\n
# @lcpr case=end

# @lcpr case=start
# [2, 1, -1]\n
# @lcpr case=end

#

