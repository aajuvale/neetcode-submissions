class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        var profit = 0
        var (ptrOne, ptrTwo) = (0, 1)
        var maxProfit = 0

        while ptrTwo < prices.count {
            if prices[ptrOne] < prices[ptrTwo] {
                profit = prices[ptrTwo] - prices[ptrOne]
                maxProfit = max(profit, maxProfit)            
            } else {
                ptrOne = ptrTwo
            } 
            ptrTwo += 1
        }
        return maxProfit
    }
}
