class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        both=min(need1,need2)
        remaining1=need1-both
        remaining2=need2-both
        price1=min(cost1,costBoth)
        price2=min(cost2,costBoth)
        totalcost=both*min(costBoth,cost1+cost2)+remaining1*price1+remaining2*price2
        return totalcost