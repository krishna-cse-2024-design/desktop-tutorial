class Solution:
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):

        def calc(start1, dur1, start2, dur2):
            min_end = float('inf')

            for i in range(len(start1)):
                min_end = min(min_end, start1[i] + dur1[i])

            ans = float('inf')

            for i in range(len(start2)):
                ans = min(ans, max(min_end, start2[i]) + dur2[i])

            return ans

        land_first = calc(
            landStartTime, landDuration,
            waterStartTime, waterDuration
        )

        water_first = calc(
            waterStartTime, waterDuration,
            landStartTime, landDuration
        )

        return min(land_first, water_first)