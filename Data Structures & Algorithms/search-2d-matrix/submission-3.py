class Solution:
    def binarySearch(self, arr, target):
        L, R = 0, len(arr) - 1

        while L <= R:
            mid = L + ((R-L)//2)
            if arr[mid] > target:
                R = mid - 1
            elif arr[mid] < target:
                L = mid + 1
            else:
                return mid
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        U, D = 0, len(matrix) - 1

        while U <= D:
            md = U + (D - U)//2
            if matrix[md][0] > target:
                D = md - 1
            elif matrix[md][-1] < target:
                U = md + 1
            else:
                break

        if not(U <= D):
            return False
        md = U + ((D - U) // 2)

        res = self.binarySearch(matrix[md], target)
        if res != -1:
            return True
    
        return False