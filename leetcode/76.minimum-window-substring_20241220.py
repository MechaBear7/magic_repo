#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30204
#
# [76] 最小覆盖子串
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        hashmap = {}
        for d in t:
            if d in hashmap:
                hashmap[d] += 1
            else:
                hashmap[d] = 1

        def check():
            for value in hashmap.values():
                if value > 0:
                    return False
            return True

        result = ""
        left, right = 0, 0
        while right < len(s):
            if s[right] in hashmap:
                hashmap[s[right]] -= 1
            while check():
                if result == "" or right - left + 1 < len(result):
                    result = s[left : right + 1]
                if s[left] in hashmap:
                    hashmap[s[left]] += 1
                left += 1
            right += 1
        return result


# @lc code=end


#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#
