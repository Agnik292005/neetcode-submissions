class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        marea=0
        for i in range(len(heights)):
            left=i
            right=i
            leftmin=heights[i]
            rightmin=heights[i]
            width=0
            while left>=0:
                if heights[left]>=heights[i]:
                    left-=1
                else:
                    break
            while right<len(heights):
                if heights[right]>=heights[i]:
                    right+=1
                else:
                    break
            width=right-left-1
            area=width*heights[i]
            if area>marea:
                marea=area
        return marea

        