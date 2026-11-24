
class Solution:
    def assignUmbrella(self, rain: List[int]) -> List[str]:
        alice = 0
        bob = 0
        ans = []

        n = len(rain)

        for i in range(n):
            if rain[i] == 0:
                ans.append("None")

            elif i < n - 1 and rain[i + 1] == 1 and alice <= bob:
                ans.append("Alice")
                alice += 1

            else:
                ans.append("Bob")
                bob += 1

        return ans
