class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        res = float('inf')

        # Case 1: land ride first, then water ride
        for i in xrange(len(landStartTime)):
            land_end = landStartTime[i] + landDuration[i]
            for j in xrange(len(waterStartTime)):
                start_water = max(land_end, waterStartTime[j])
                res = min(res, start_water + waterDuration[j])

        # Case 2: water ride first, then land ride
        for j in xrange(len(waterStartTime)):
            water_end = waterStartTime[j] + waterDuration[j]
            for i in xrange(len(landStartTime)):
                start_land = max(water_end, landStartTime[i])
                res = min(res, start_land + landDuration[i])

        return res