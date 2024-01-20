class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        print(s,t)
        already_mapped = {}
        already_mapped2 = {}
        built_str =""
        if len(s)!= len(t):
            print("wrong length")
            return False
        if s == t:
            print("same string")
            return True
        for i in range(len(s)):
            try:
                if already_mapped[s[i]] !=t[i]:
                    print("already mapped")
                    return False
                
            except KeyError:
                already_mapped[s[i]] = t[i]
            try:
                if already_mapped2[t[i]] != s[i]:
                    print("already mapped")
                    return False
            except KeyError:
                already_mapped2[t[i]] = s[i]
            built_str+=s[i]
            print(already_mapped, already_mapped2, s, t, built_str)
        if built_str == s:
            return True
        print(built_str,s)
        print("falsed out")

        return False