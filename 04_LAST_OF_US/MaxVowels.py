class Solution6:
    def maxVowels(self, s: str, k: int) -> int:
        current_vowel_count = 0

        def is_vowel(ci):
            if ci in {'a', 'e', 'i', 'o', 'u'}:
                return True
            return False

        current_count = 0
        for i in range(k - 1):
            if is_vowel(s[i]):
                current_count += 1

        # if k = 3, the above will go from 0 to 1
        # now want to go from i = 2
        # for an i (2), then first char is (i - (k - 1))

        max_vs = 0
        for i in range(k - 1, len(s)):
            if is_vowel(s[i]):
                current_count += 1

            max_vs = max(max_vs, current_count)

            if is_vowel(s[i - (k - 1)]):
                current_count -= 1
        return max_vs


s = Solution6()
print(3 == s.maxVowels("abciiidef", 3))
print(2 == s.maxVowels("aeiou", 2)) 