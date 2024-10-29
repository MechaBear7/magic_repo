#
# @lc app=leetcode.cn id=383 lang=python3
# @lcpr version=30204
#
# [383] 赎金信
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        hashmap = {}
        for s in magazine:
            hashmap[s] = hashmap.get(s, 0) + 1

        for s in ransomNote:
            if s not in hashmap or hashmap[s] == 0:
                return False
            hashmap[s] -= 1
        return True


# @lc code=end


#
# @lcpr case=start
# "a"\n"b"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"ab"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"aab"\n
# @lcpr case=end

#
