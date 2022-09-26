class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        (1) Initialize array of leading zeroes len(num1+num2)
        (2) 2 for-loops, with each successive 2-for-loops, we will multiple num1[i] * num2[j] and manage the carry
        (2.1) managing carry:
        step 1: multiply num1[i] * num2[j]
        step 2: add the initialized_array[i+j] with step1
        step 3: set initialized_array[i+j] with current non-carry  (%10)
        step 4: add initialized_array[i+j + 1] with the carry (//10)
        (3) removing leading 0 and perform a join
        '''
        # edge-case
        if '0' in [num1, num2]:
            return '0'
        res = [0] * (len(num1)+len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                curRes = int(num1[i]) * int(num2[j])
                curRes += res[i+j]
                res[i+j] = curRes % 10
                res[i+j+1] += curRes // 10 
        index = len(res) - 1
        while index > 0 and res[index] == 0:
            index -= 1
        res = [str(x) for x in res[0:index+1]]
        return ''.join(res[::-1])
                
                
                
        
        