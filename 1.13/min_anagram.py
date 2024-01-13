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
            extra_letters = []
            for letter in string:
                try:
                    dictionary[letter]-=1
                except:
                    extra_letters.append(letter)
            print(dictionary)
            print(extra_letters)
          
            positive = 0
            
            for value in dictionary.values():
                if value == 0:
                    continue
                elif value <= 0:
                    for _ in range(value*-1):
                        extra_letters.append("a")
                else:
                    positive+=1
            amount_extra_letter = len(extra_letters)
            print(positive)
            if amount_extra_letter >= positive:
                return amount_extra_letter
            answer = ((positive )/2 - (positive)%2 + amount_extra_letter)
            return answer

        number_of_changes = sub_dict(s_dict, t)
        
        return int(number_of_changes)


