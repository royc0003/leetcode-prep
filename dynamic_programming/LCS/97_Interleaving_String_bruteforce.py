class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        def bruteforce(i1, i2, i3):
            '''
            Time Complexity: O(2^(N+M))
            '''
            if i1 >= len(s1) or i2 >= len(s2) or i3 >= len(s3):
                return True
            
            c1, c2 = False, False
            if s1[i1] == s3[i3]:
                c1 = bruteforce(i1+1, i2, i3+1)
            elif s2[i2] == s3[i3]:
                c2 = bruteforce(i1, i2+1, i3+1)
            
            return (c1 or c2)

        return bruteforce(0, 0, 0)

