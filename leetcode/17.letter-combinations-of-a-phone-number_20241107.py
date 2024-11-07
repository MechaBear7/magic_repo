#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30204
#
# [17] 电话号码的字母组合
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        hashmap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def backtracking(result, path, rest_digits):
            if len(rest_digits) == 0:
                result.append("".join(path[:]))
                return
            cur_digit = rest_digits[0]
            for d in hashmap[cur_digit]:
                path.append(d)
                backtracking(result, path, rest_digits[1:])
                path.pop()

        result = []
        backtracking(result, [], digits)
        return result


# @lc code=end


#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#
