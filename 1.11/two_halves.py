class Solution:
    def halvesAreAlike(self, s):
        vowel_count = 0
        vowels = "aeiouAEIOU"
        half = int(len(s) / 2)
        first_half = s[:half]
        second_half = s[half:]
        for letter in first_half:
            if letter in vowels:
                vowel_count+=1
        for letter in second_half:
            if letter in vowels:
                vowel_count-=1
        return vowel_count == 0