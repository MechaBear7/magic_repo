#
# @lc app=leetcode.cn id=217 lang=python3
# @lcpr version=30204
#
# [217] 存在重复元素
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for num in nums:
            if num not in my_set:
                my_set.add(num)
            else:
                return True
        return False


# @lc code=end


#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,3,3,4,3,2,4,2]\n
# @lcpr case=end

#
