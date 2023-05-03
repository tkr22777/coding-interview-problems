/*
 https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
 Find the maximum profit you can make with at most two transactions.
*/
class BuySellStockIII {

    public static void main(String[] args) {
        int[] ar = {3,3,5,0,0,3,1,4};
        System.out.println(new BuySellStockIII().maxProfit(ar));
    }

    // returns maximum profit possible from single transaction going forward from day i
    private int[] maxSingleTxnProfit(int[] prices) {
        int[] maxSingleTxnProfit = new int[prices.length];

        int maxProfitI = 0;
        int maxSellPrice = prices.length > 0 ? prices[prices.length - 1]: 0;
        for (int i = prices.length - 1; i >= 0 ; --i) {
            if (maxSellPrice < prices[i]) {
                maxSellPrice = prices[i];
            }
            int buyProfitI = maxSellPrice - prices[i];
            maxProfitI = Math.max(maxProfitI, buyProfitI);
            maxSingleTxnProfit[i] = maxProfitI;
        }
        return maxSingleTxnProfit;
    }

    public int maxProfit(int[] prices) {
        int[] maxBuyProfitForSingleTxnDays = maxSingleTxnProfit(prices);

        int maxTwoTxnProfit = 0;
        int minBuyPrice = prices.length > 0 ? prices[0]: 0;
        for (int i = 0; i < prices.length; i++) {
            if (minBuyPrice > prices[i]) {
                minBuyPrice = prices[i];
            } 
            int sellProfitI = prices[i] - minBuyPrice;
            int nextMaxBuyProfit = 0;
            if (i + 1 < maxBuyProfitForSingleTxnDays.length) {
                nextMaxBuyProfit = maxBuyProfitForSingleTxnDays[i + 1];
            }
            maxTwoTxnProfit = Math.max(maxTwoTxnProfit, sellProfitI + nextMaxBuyProfit);
        }
        return maxTwoTxnProfit;
    }
}

