class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        charToNum = {'0' : 0, '1': 1, '2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8':8,'9':9}
        res = [0] * (len(num1) + len(num2))
        resIndex = 0
        
        def calCarry(nums2, nums1, resIndex, j):
            '''
            15 % 10 == 5 (non-carry)
            15 // 10 = 1 (carry)
            res = [0,0,0,0,0,0]
            1 2 3
            4 5 6
            mulRes 
            '''
            carry = 0
            j = j // len(num1)
            nums2Int, nums1Int = charToNum[nums2], charToNum[nums1]
            # Step 1: multiply both
            mulRes = nums2Int * nums1Int
            # Step 2: Add current res array to multiplied
            mulRes += res[resIndex+j]
            # Step 3: find the overall carry
            carry += mulRes // 10 
            # Step 4: add the carry and non-carry to the result array
            res[resIndex+j] = mulRes % 10 
            res[resIndex + 1 + j] += carry if resIndex + j + 1 < len(res) else None
            
            
        
        for i in range(len(num2)-1,-1,-1):
            for j in range(len(num1)-1,-1,-1):
                calCarry(num2[i], num1[j], resIndex,j)
            resIndex += 1
        res = [str(x) for x in res if x != 0]
        return ''.join(res[::-1])
        
        
        
        
        
        