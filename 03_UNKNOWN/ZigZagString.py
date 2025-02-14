#!/usr/bin/python

"""

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""

class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 0 or numRows == 1:
            return s

        charList = list(s)

        if len(charList) < numRows:
            return s

        rows = [];
        for i in range(0, numRows):
            rows.append([])

        i = 0
        increase = True
        for aChar in charList:

            rows[i].append(aChar);

            if i == numRows - 1:
                increase = False
            if i == 0:
                increase = True

            if increase:
                i = i + 1
            else:
                i = i - 1

        returnString = []

        for row in rows:
            returnString.append(''.join(row));

        return ''.join(returnString)

zigZag = Solution();

print zigZag.convert("AB",1)
print zigZag.convert("hjouvsuyoypayulyeimuotehzriicfskpggkbbipzzrzucxamludfykgruowzgiooobppleqlwphapjnadqhdcnvwdtxjbmyppphauxnspusgdhiixqmbfjxjcvudjsuyibyebmwsiqyoygyxymzevypzvjegebeocfuftsxdixtigsieehkchzdflilrjqfnxztqrsvbspkyhsenbppkqtpddbuotbbqcwivrfxjujjddntgeiqvdgaijvwcyaubwewpjvygehljxepbpiwuqzdzubdubzvafspqpqwuzifwovyddwyvvburczmgyjgfdxvtnunneslsplwuiupfxlzbknhkwppanltcfirjcddsozoyvegurfwcsfmoxeqmrjowrghwlkobmeahkgccnaehhsveymqpxhlrnunyfdzrhbasjeuygafoubutpnimuwfjqsjxvkqdorxxvrwctdsneogvbpkxlpgdirbfcriqifpgynkrrefx", 503)


