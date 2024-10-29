#
# @lc app=leetcode.cn id=219 lang=python3
# @lcpr version=30204
#
# [219] 存在重复元素 II
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_set = set()
        left_idx = 0
        for right_idx in range(len(nums)):
            if right_idx - left_idx > k:
                my_set.remove(nums[left_idx])
                left_idx += 1
            if nums[right_idx] in my_set:
                return True
            else:
                my_set.add(nums[right_idx])
        return False


# @lc code=end


#
# @lcpr case=start
# [1,2,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,2,3]\n2\n
# @lcpr case=end

#
