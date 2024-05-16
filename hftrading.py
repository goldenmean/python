'''
You are given the list of prices of a particular stock. Each element in the array represents the price of
the stock at a given second throughout the current day. Return the maximum profit you can make trading this stock.
Note: You may only ever buy and sell a single share of the stock, but you may make multiple transactions (i.e. buys and sells).
Ex: Given the following prices...

prices = [8, 3, 2, 4, 6, 4, 5], return 5.
explanation: buy when 2, sell when 6, profit = 4
buy when 4 and sell when 5, profit = 1. 
Total profit is 4 + 1 = 5
'''

def hftrading(prices):
    l=0
    curprofit = 0
    maxprofit = 0
    total = 0
    for r in range(1,len(prices)):
        curprofit = prices[r]-prices[l]
        if curprofit <= 0:
            l+=1
        else:
            #profit is positive
            #get the maximux
            if curprofit < maxprofit:
                #if current profit is lesser than previous max profit, then time to sell the share
                maxprofit = max(maxprofit, curprofit)
                #book the max profit total
                total+=maxprofit
                #reset max profit to zero for new trade
                maxprofit = 0
                #set buy price as current price
                l=r
            else:
                #if current profit is more than previous max profit , continue to hold the share
                maxprofit = max(maxprofit, curprofit)

    total+=maxprofit        
    return total
         
prices = [8, 3, 2, 4, 6, 4, 5]
total=hftrading(prices)
print(f"Total profit is {total}")