class DetectSquares:
    '''
    (0,0)(0,1)
    (1,0)(1,1)
    
    
    '''

    def __init__(self):
        self.freqCount = defaultdict(int)
        self.pnts = [] 
        

    def add(self, point: List[int]) -> None:
        self.freqCount[tuple(point)] += 1
        self.pnts.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0 
        px, py = point
        # step 1: find all the diagonals; y2-x2+x1 = y1
        for x,y in self.pnts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res +=   self.freqCount[(x,py)] * self.freqCount[(px,y)]
        # step 2: 
        return res
            
        
        
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)