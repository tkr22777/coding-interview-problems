from collections import deque

# The following is not the right way as it is way simpler to use
# loop over str1 and str2 with two pointers where they can just 
# increase and match until str2's end
# there's no need for the BFS like queueing (which is simply doing that)
# re-write in future
class Solution02:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        q = deque()
        q.append((0, 0))
        ls1 = len(str1)
        ls2 = len(str2)
        while q:
            # print(q)
            # print(visited)
            indices = q.pop()
            i, j = indices[0], indices[1]
            if i >= ls1:
                continue

            if ls1 - i < ls2 - j:
                continue

            if str1[i] == str2[j] or (str1[i] == 'z' and str2[j] == 'a') or (ord(str1[i]) + 1 == ord(str2[j])):
                if j + 1 == ls2:
                    return True
                q.append((i + 1, j + 1))
            else:
                q.append((i + 1, j))
        return False


s = Solution02()
print(s.canMakeSubsequence("abc", "ad") == True)
print(s.canMakeSubsequence("zc", "ad") == True)
print(s.canMakeSubsequence("ab", "d") == False)
print(s.canMakeSubsequence("uuwqhbotpibvgdkclslnebjpovdsbgunvvbwasplya", "vuwhptivelcmtnfbkppdtuowvcwasqa") == True)