class Solution:
    def pushZerosToEnd(self, arr, n):
        pos = 0   # next index to place a non-zero
        
        # move all non-zero elements forward
        for i in range(n):
            if arr[i] != 0:
                arr[pos] = arr[i]
                pos += 1
        
        # fill the rest with zeros
        while pos < n:
            arr[pos] = 0
            pos += 1


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    n = int(input("Enter size of array: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    obj = Solution()
    obj.pushZerosToEnd(arr, n)

    print("Array after moving zeros:", arr)