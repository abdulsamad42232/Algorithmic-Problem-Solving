class Solution:
    def maxArea(self, height: List[int]) -> int:
        areas=[]
        left=0
        right=len(height)-1
        while left<right:
            if height[left]<=height[right]:
                length=height[left]
                breadth=right-left
                area=length*breadth
                areas.append(area)
                left +=1
            elif height[left]>height[right]:
                length=height[right]
                breadth=right-left
                area=length*breadth
                areas.append(area)
                right-=1
            else:
                pass
        return(max(areas))





