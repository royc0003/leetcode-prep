class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index: height)
        maxHeight = 0 
        
        # 1st pass: check forward to ensure that items are only in ascending order
        # and for items that violate, pop them until valid. 
        # the valid item's index will be extended backwards to the last popped index
        # to maximize area for 2nd pass
        for i,h in enumerate(heights):
            # create a start index
            start = i 
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxHeight = max(maxHeight, height * (i - index))
                start = index
            # append the new index
            stack.append((start, h))
        
        # 2nd pass: calculate the maximize area possible
        for i,h in stack:
            maxHeight = max(h * (len(heights) - i), maxHeight)
        
        return maxHeight
        
        
        
        