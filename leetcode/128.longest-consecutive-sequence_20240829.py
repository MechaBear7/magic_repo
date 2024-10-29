#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30204
#
# [128] 最长连续序列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()
        for num in nums:
            my_set.add(num)
        max_length = 0
        for num in nums:
            length = 0
            if num in my_set:
                length += 1
                my_set.remove(num)
                left_num, right_num = num - 1, num + 1
                while left_num in my_set:
                    my_set.remove(left_num)
                    length += 1
                    left_num -= 1
                while right_num in my_set:
                    my_set.remove(right_num)
                    length += 1
                    right_num += 1
            max_length = max(max_length, length)
        return max_length


# @lc code=end


#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

#
