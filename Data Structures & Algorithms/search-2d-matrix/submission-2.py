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
        for row in range(len(matrix)):
            print(row)
            if matrix[row][-1] >= target:
                res = self.binarySearch(matrix[row], target)
                if res != -1:
                    return True
        return False