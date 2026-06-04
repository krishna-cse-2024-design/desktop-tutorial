class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        total_score = 0
        
        # Iterate over all numbers in the inclusive range
        for num in range(num1, num2 + 1):
            s = str(num)
            length = len(s)
            
            # Numbers with fewer than 3 digits have a waviness of 0
            if length < 3:
                continue
                
            # Check every interior digit
            for i in range(1, length - 1):
                prev_digit = s[i - 1]
                curr_digit = s[i]
                next_digit = s[i + 1]
                
                # Check for Peak or Valley conditions
                if (curr_digit > prev_digit and curr_digit > next_digit) or \
                   (curr_digit < prev_digit and curr_digit < next_digit):
                    total_score += 1
                    
        return total_score