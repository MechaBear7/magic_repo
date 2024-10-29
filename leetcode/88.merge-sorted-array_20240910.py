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
        p, p1, p2 = m + n - 1, m - 1, n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p, p1 = p - 1, p1 - 1
            else:
                nums1[p] = nums2[p2]
                p, p2 = p - 1, p2 - 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p, p2 = p - 1, p2 - 1


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
