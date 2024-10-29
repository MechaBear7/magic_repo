#
# @lc app=leetcode.cn id=88 lang=python3
# @lcpr version=30204
#
# [88] 合并两个有序数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = m - 1
        n2 = n - 1
        tail = m + n - 1
        while n1 >= 0 and n2 >= 0:
            if nums1[n1] > nums2[n2]:
                nums1[tail] = nums1[n1]
                n1 = n1 - 1
            else:
                nums1[tail] = nums2[n2]
                n2 = n2 - 1
            tail -= 1
        while n2 >= 0:
            nums1[tail] = nums2[n2]
            n2 -= 1
            tail -= 1
        

# @lc code=end



#
# @lcpr case=start
# [1,2,3,0,0,0]\n3\n[2,5,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n[]\n0\n
# @lcpr case=end

# @lcpr case=start
# [0]\n0\n[1]\n1\n
# @lcpr case=end

#

