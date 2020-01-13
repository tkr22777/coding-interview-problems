class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        return self.match(s, p, 0, 0, {})

    def match(self, s, p, si, pi, memo):

        if si in memo and pi in memo[si]:
            return memo[si][pi]

        #print "s:" + str(s[si:]) + " p:" + str(p[pi:]) + " si: " + str(si) + " pi:" + str(pi)

        if si == len(s) and pi == len(p):
            #print "Here is a match"
            return True

        if pi >= len(p):
            return False

        if si >= len(s):
            if self.checkStar(p[pi:]):
                return True
            else:
                return False

        if p[pi] == '*':
            if self.match(s, p, si, pi + 1, memo): #did not use *
                return self.setAnReturn(memo, si, pi, True)
            if self.match(s, p, si + 1, pi + 1, memo): #used * for a char
                return self.setAnReturn(memo, si, pi, True)
            match = self.match(s, p, si + 1, pi, memo)) #used * for one or more chars
            return self.setAnReturn(memo, si, pi, match)

        if p[pi] == '?' or p[pi] == s[si]:
            match = self.match(s, p, si + 1, pi + 1, memo) 
            return self.setAnReturn(memo, si, pi, match)

        return False

    def checkStar(self, aStr):
        for char in aStr:
            if char != '*':
                return False
        return True

    def setAnReturn(self, memo, si, pi, val):
        if si not in memo:
            memo[si] = {}
        memo[si][pi] = val
        return val

