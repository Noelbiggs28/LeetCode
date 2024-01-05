class Solution:
    def findContentChildren(self, g, s):
        satisifed_children = 0
        s = sorted(s, reverse=True)
        g = sorted(g, reverse=True)
        index = 0
        cookies = len(s)
        for child in g:
            if cookies == index:
                break
            if child <= s[index]:
                satisifed_children+=1
                index +=1

        return satisifed_children