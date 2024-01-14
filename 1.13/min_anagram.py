class Solution:
    def minSteps(self, s: str, t: str) -> int:
        def make_dict(string):
            temp_dict = {}
            unique = set(string)
            for letter in unique:
                temp_dict[letter] = 0
            for letter in string:
                temp_dict[letter] +=1
            return temp_dict
        s_dict = make_dict(s)
        def sub_dict(dictionary, string):
            extra_letters = 0
            for letter in string:
                try:
                    dictionary[letter]-=1
                except:
                    extra_letters +=1
            positive = 0
            for value in dictionary.values():
                if value == 0:
                    continue
                elif value <= 0:
                    extra_letters += (value*-1)
                else:
                    positive+=1
            if extra_letters >= positive:
                return extra_letters
            answer = (positive /2 + extra_letters)
            return answer
        number_of_changes = sub_dict(s_dict, t)
        return int(number_of_changes)