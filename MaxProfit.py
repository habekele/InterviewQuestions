def maxProfit(prices):
    
    profit = 0
    for count,value in enumerate(prices):
        for y in prices[count+1::]:
            if (y-value) > profit:
                profit = y-value
            

    
    return profit

def maxProfit2(prices):
    Mprofit = 0
    l = 0
    r = 1

    while r < len(prices):
        
        if prices[r] > prices[l]:
            Mprofit = max(Mprofit, prices[r] - prices[l])
        else:
            l = r
        r += 1
    return Mprofit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit2([7,1,5,3,6,4]))
    

