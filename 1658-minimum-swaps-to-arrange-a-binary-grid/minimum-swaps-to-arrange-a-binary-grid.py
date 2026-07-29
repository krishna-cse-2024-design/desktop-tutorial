class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        temp = []
        
        # Count trailing zeros for each row
        for row in grid:
            i = n - 1
            cnt = 0
            while i >= 0 and row[i] == 0:
                i -= 1
                cnt += 1
            temp.append(cnt)
        
        ans = 0
        cur_len = n - 1
        
        # Greedily place rows
        for i in range(n):
            j = i
            
            # Find a row with enough trailing zeros
            while j < n and temp[j] < cur_len:
                j += 1
            
            if j == n:
                return -1
            
            # Bring row j up to position i using adjacent swaps
            for k in range(j, i, -1):
                temp[k], temp[k - 1] = temp[k - 1], temp[k]
                ans += 1
            
            cur_len -= 1
        
        return ans