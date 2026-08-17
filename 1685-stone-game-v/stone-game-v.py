class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        
        @cache
        def find_max_score(first: int, last: int, total_sum: int) -> int:
            #print(first, last, total_sum)

            length = last - first
            if length <= 1:
                return 0
            #if length == 2:
            #    return min(stoneValue[first], stoneValue[first + 1])

            half_sum = total_sum / 2

            left_sum = 0
            for i, num in enumerate(stoneValue[first:last], start=first):
                left_sum += num
                if left_sum >= half_sum:
                    break

            max_score = 0

            left_i = right_i = i
            right_sum = total_sum - left_sum
            if left_sum > half_sum:
                left_sum -= stoneValue[i]
                left_i -= 1

            j = left_i + 1
            while 2 * left_sum > max_score:
                score = left_sum + find_max_score(first, j, left_sum)
                if max_score < score:
                    max_score = score
                j -= 1
                left_sum -= stoneValue[j]

            j = right_i + 1
            while 2 * right_sum > max_score:
                score = right_sum + find_max_score(j, last, right_sum)
                if max_score < score:
                    max_score = score
                right_sum -= stoneValue[j]
                j += 1
                
            #print(first, last, total_sum, max_score)

            return max_score

        return find_max_score(0, len(stoneValue), sum(stoneValue))