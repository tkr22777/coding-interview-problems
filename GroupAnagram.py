class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        output = []
        outMap = {}

        for i in range(0, len(strs)):

            key = ''.join(sorted(strs[i]))

            if key in outMap:
                aList = outMap.get(key)
                aList.append(strs[i])
            else:
                aList = []
                aList.append(strs[i])
                outMap[key] = aList

        for val in outMap.values():
            output.append(val)

        return output


s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
