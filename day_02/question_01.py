def bestTimeToSellStocks(arr):
    minimum=max(arr)
    maxProfit=0
    for i in arr:
        minimum=min(minimum,i)
        maxProfit=max(maxProfit,i-minimum)
    return maxProfit
print(bestTimeToSellStocks([7,1,5,3,6,4]))
