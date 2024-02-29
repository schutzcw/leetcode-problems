from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(-1, -1*len(digits)-1, -1):
            print(i)
            digit = digits[i] + 1
            if digit < 10:
                digits[i] = digit
                return digits
            digits[i] = 0
        # if we made it this far we need to expand the list by a digit
        return [1] + digits


if __name__ == "__main__":
    s = Solution()
    # print(s.plusOne([1, 2, 3]))  # [1,2,4]
    # print(s.plusOne([4, 3, 2, 1]))  # [4,3,2,2]
    # print(s.plusOne([4, 3, 9, 9]))  # [4,4,0,0]
    print(s.plusOne([9, 9, 9, 9]))  # [1,0,0,0,0]
    print(s.plusOne([9]))  # [1,0]
