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
        ptr_nums1 = m - 1
        ptr_nums2 = n - 1
        ptr_input = m + n - 1
        while ptr_nums1 >= 0 and ptr_nums2 >= 0:
            if nums1[ptr_nums1] > nums2[ptr_nums2]:
                nums1[ptr_input] = nums1[ptr_nums1]
                ptr_input -= 1
                ptr_nums1 -= 1
            else:
                nums1[ptr_input] = nums2[ptr_nums2]
                ptr_input -= 1
                ptr_nums2 -= 1
        while ptr_nums1 >= 0:
            nums1[ptr_input] = nums1[ptr_nums1]
            ptr_input -= 1
            ptr_nums1 -= 1
        while ptr_nums2 >= 0:
            nums1[ptr_input] = nums2[ptr_nums2]
            ptr_input -= 1
            ptr_nums2 -= 1


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
