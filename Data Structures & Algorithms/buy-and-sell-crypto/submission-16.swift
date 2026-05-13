class Solution {
     func maxProfit(_ prices: [Int]) -> Int {
        var (L, R) = (0, 1)
        var maxProfit = 0
        var profit = 0

        while R < prices.count {
            if prices[L] < prices[R] {
                profit = prices[R] - prices[L]
                maxProfit = max(maxProfit, profit)
            } else {
                L = R
            }
            R += 1
        }

        return maxProfit
    }
}
