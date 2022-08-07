class Solution (object):
    def countVowelPermutation (self, n):
        """
        :type n:int
        :rtype: int
        """
        dp = [[0] * 5 for i in range(n)]
        vowels = ['a', 'e', 'i', 'o', 'u']
        dp [0][0] = dp [0][1] = d= dp [0][2] = dp [0][3] = dp [0][4] = 1

        for i in range(1, len(dp)):
            for j in range(len(vowels)):
                if vowels [j] == 'a':
                    dp [i][j] += dp [i - 1][vowels.index('e')]
                    dp [i][j] += dp [i - 1][vowels.index('u')]
                    dp [i][j] += dp [i - 1][vowels.index('i')]
                elif vowels [j] == 'e':
                    dp [i][j] += dp [i - 1][vowels.index('a')]
                    dp [i][j] += dp [i - 1][vowels.index('i')]
                elif vowels [j] == 'i':
                    dp [i][j] += dp [i - 1][vowels.index('e')]
                    dp [i][j] += dp [i - 1][vowels.index('o')]
                elif vowels [j] == 'o':
                    dp [i][j] += dp [i - 1][vowels.index('i')]
                elif vowels [j] == 'u':
                    dp [i][j] += dp [i - 1][vowels.index('i')]
                    dp [i][j] += dp [i - 1][vowels.index('o')]
        return sum (dp[-1]) % (10**9 + 7)
