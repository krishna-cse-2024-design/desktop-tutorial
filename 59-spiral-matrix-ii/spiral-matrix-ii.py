class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[0]*n for _ in range(n)]

        top,down = 0, n
        left,right = 0, n

        count = 1

        while top <= down and left <= right:

            # top left to top right
            for c in range(left, right, 1):
                output[top][c] = count
                count +=1
            top += 1
            
            # top right to down right
            for r in range(top, down, 1):
                output[r][right-1] = count
                count +=1
            right -=1

            # down right to donw left
            for c in range(right-1,left-1, -1):
                output[down-1][c] = count
                count +=1
            down -=1

            # down right to top left
            for r in range(down-1,top-1, -1):
                output[r][left] = count
                count +=1
            left += 1

        return output