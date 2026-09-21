class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for character in s:
            if character.isalnum():
                newStr += character.lower()
        return newStr == newStr[:: -1]


        