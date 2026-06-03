class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[0]*len(height)
        rightmax=[0]*len(height)
        mleft=0
        mright=0
        for i in range(len(height)):
            curleft=height[i]
            curright=height[len(height)-i-1]
            if curleft>mleft:
                mleft=curleft
            if curright>mright:
                mright=curright
            leftmax[i]=mleft
            rightmax[len(height)-i-1]=mright
        s=0
        for i in range(len(height)):
            s+=min(leftmax[i],rightmax[i])-height[i]
        return s

            
        