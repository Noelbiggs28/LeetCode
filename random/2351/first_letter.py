class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letters = []
        for letter in s:
            if letter in letters:
                return letter
            else:
                letters.append(letter)