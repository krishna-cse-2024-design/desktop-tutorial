class Solution:
    def removeCoveredIntervals(self, a: List[List[int]]) -> int:
        return sum(sum(ll<=l<r<=rr for ll,rr in a)==1 for l,r in a)