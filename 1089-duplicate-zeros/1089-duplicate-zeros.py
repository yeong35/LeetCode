class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        length = len(arr)

        while(i < length):
            if arr[i] == 0:
                arr = arr[:i+1] + [0] + arr[i+1:len(arr)-1]
                i += 1
            i += 1
        
        
        print(arr)
        """
        Do not return anything, modify arr in-place instead.
        """
        