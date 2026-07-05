class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        limit = n - 1
        
        # O(N) Space: Track only the row below us
        next_score = [-1] * n
        next_count = [0] * n
        
        # Base Case Setup on the bottom-most row boundary
        next_score[limit] = 0
        next_count[limit] = 1
        
        # Process the grid bottom-up, row by row
        for r in range(limit, -1, -1):
            board_row = board[r]
            
            # Temporary arrays for the current row we are computing
            curr_score = [-1] * n
            curr_count = [0] * n
            
            # Special case handling for the starting cell on the very first loop pass
            if r == limit:
                curr_score[limit] = 0
                curr_count[limit] = 1
            
            for c in range(limit, -1, -1):
                # Skip the starting cell execution flow and obstacles
                if (r == limit and c == limit) or board_row[c] == 'X':
                    continue
                
                best_score = -1
                ways = 0
                
                # Direction 1: Look Down (Pushed from next_score row array)
                if r < limit:
                    s_down = next_score[c]
                    if s_down > best_score:
                        best_score = s_down
                        ways = next_count[c]
                    elif s_down == best_score and s_down != -1:
                        ways = (ways + next_count[c]) % MOD
                
                # Direction 2: Look Right (Pulled from our active curr_score row array)
                if c < limit:
                    s_right = curr_score[c + 1]
                    if s_right > best_score:
                        best_score = s_right
                        ways = curr_count[c + 1]
                    elif s_right == best_score and s_right != -1:
                        ways = (ways + curr_count[c + 1]) % MOD
                        
                # Direction 3: Look Down-Right Diagonal (Pushed from next_score row array)
                if r < limit and c < limit:
                    s_diag = next_score[c + 1]
                    if s_diag > best_score:
                        best_score = s_diag
                        ways = next_count[c + 1]
                    elif s_diag == best_score and s_diag != -1:
                        ways = (ways + next_count[c + 1]) % MOD
                
                # Commit finalized state if cell is accessible
                if best_score != -1:
                    char = board_row[c]
                    current_val = 0 if char == 'E' else (ord(char) - 48)
                    curr_score[c] = best_score + current_val
                    curr_count[c] = ways
            
            # Shift state: Current row becomes the "next row" for the loop step above
            next_score = curr_score
            next_count = curr_count
                    
        # Grab destination states from the top-leftmost indices of our shifted row arrays
        final_score = next_score[0]
        if final_score == -1:
            return [0, 0]
            
        return [final_score, next_count[0]]