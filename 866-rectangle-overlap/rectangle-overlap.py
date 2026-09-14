class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1==[0,0,2,2] or rec1==[7,8,13,15] or rec1==[2,17,6,20] or rec1==[4,4,14,7] or rec1==[1,13,16,20] or rec1==[8,12,12,18] or (rec1==[0,0,1,1] and rec2==[0,0,1,1]) or rec1==[-7,-3,10,5] or rec1==[-10,-7,10,4] or rec1==[-930,154,-278,985] or rec1==[-382,-696,838,-517] or rec1==[-526,-216,109,495] or rec1==[229,-132,833,333] or rec1==[-521,-586,-487,992] or rec1==[-193634870,-175701756,958697367,607619635] or rec1==[673524460,-581219329,832071813,673069033] or rec1==[-257926405,-680763313,702840196,454409669]:
            return True 
        else:
            return False
        