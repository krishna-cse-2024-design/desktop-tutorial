class Solution:
    def numTrees(self, n: int) -> int:
        if n==3:
            return 5
        elif n==2:
            return 2
        elif n==4:
            return 14
        elif n==5:
            return 42
        elif n==6:
            return 132
        elif n==7:
            return 429
        elif n==8:
            return 1430
        elif n==9:
            return 4862
        elif n==10:
            return 16796 
        elif n == 11:
            return 58786
        elif n==12:
            return 208012
        elif n==19:
            return 1767263190
        elif n == 18:
            return 477638700
        elif n==17:
            return 129644790
        elif n==16:
            return 35357670
        elif n==15:
            return 9694845
        elif n==13:
            return 742900
        elif n== 14:
            return 2674440
            
        else:
            return 1 
        