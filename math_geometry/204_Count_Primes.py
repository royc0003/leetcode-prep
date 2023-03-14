class Solution:
    def countPrimes(self, n: int) -> int:

        is_prime = [True] * n
        
        if len(is_prime) >= 1:
            is_prime[0] = False
        if len(is_prime) >= 2:
            is_prime[1] = False

        for i in range(2, n):
            # we only run till square root
            if (i*i) >= n:
                break
            # multiples of i cannot be prime
            if is_prime[i]:
                for j in range(2*i, n, i):
                    is_prime[j] = False

        count = 0
        for item in is_prime:
            count += 1 if item == True else 0
        return count
