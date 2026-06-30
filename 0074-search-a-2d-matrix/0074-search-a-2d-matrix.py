class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list=[]
        for sublist in matrix:
            flat_list.extend(sublist)
        l, r = 0, len(flat_list)-1
        while l<=r:
            mid = (l+r)//2
            if target>flat_list[mid]:
                l = mid + 1
                mid = (l+r)//2
            elif target<flat_list[mid]:
                r = mid - 1
                mid = (l+r)//2
            elif target == flat_list[mid]:
                return True
            else:
                pass
        return False
            

        