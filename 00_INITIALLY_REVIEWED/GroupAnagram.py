class Solution(object):
    
    def groupAnagrams(self, strs):
        outMap = {}
        for str in strs:
            key = ''.join(sorted(str))
            outMap.setdefault(key, []).append(str)

        output = []
        for val in outMap.values():
            output.append(val)
        return output


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
