class Solution(object):
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        outMap = {}
        for str in strs):
            key = ''.join(sorted(strs[i]))
            outMap.setdefault(key, []).append(strs[i])

        output = []
        for val in outMap.values():
            output.append(val)
        return output


s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
