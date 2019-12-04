class BuySellStockIII {

    public static void main(String[] args) {
        int[] ar = {3,3,5,0,0,3,1,4};
        System.out.println(new BuySellStockIII().maxProfit(ar));
    }

    public int maxProfit(int[] prices) {

        int[] singleTxnProfit = new int[prices.length];

        int maxProfit = 0;
        int maxSellPrice = prices.length > 0 ? prices[prices.length - 1]: 0;
        for (int i = prices.length - 1; i >= 0 ; --i) {
            if (prices[i] > maxSellPrice) {
                maxSellPrice = prices[i];
            } 
            maxProfit = Math.max(maxProfit, maxSellPrice - prices[i]);
            singleTxnProfit[i] = maxProfit;
        }

        maxProfit = 0;
        int minBuyPrice = prices.length > 0 ? prices[0]: 0;
        for (int i = 0; i < prices.length; i++) {
            if (minBuyPrice > prices[i]) {
                minBuyPrice = prices[i];
            } 
            int currentProfit = prices[i] - minBuyPrice;
            int nextProfit = i + 1 < singleTxnProfit.length ? singleTxnProfit[i + 1]: 0;
            maxProfit = Math.max(maxProfit, currentProfit + nextProfit);
        }
        return maxProfit;
    }
}

