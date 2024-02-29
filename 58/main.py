from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        for i in range(1, len(s)):
            print(f"i: {i}")
            if s[-1*i] == " ":
                return i-1
        return len(s)


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))  # 5
    print(s.lengthOfLastWord("   fly me   to    the moon  "))  # 4
    print(s.lengthOfLastWord("luffy is still joyboy"))  # 6
    print(s.lengthOfLastWord("b a "))  # 1
