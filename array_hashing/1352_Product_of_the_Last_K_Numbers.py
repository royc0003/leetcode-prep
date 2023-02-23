class ProductOfNumbers:
    # O(1) complexity
    
    def __init__(self):
        self.prefix_product = []
        self.num = 1
        

    def add(self, num: int) -> None:
        if num != 0:
            self.num *= num
            self.prefix_product.append(self.num)
        else:
            self.num = 1
            self.prefix_product = []

        
    def getProduct(self, k: int) -> int:
        # last k element's formulate::
        # array[-1] // array[-1-k]
        if len(self.prefix_product) < k:
            return 0
        if k == len(self.prefix_product):
            return self.prefix_product[-1]

        return self.prefix_product[-1] // self.prefix_product[-1-k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)