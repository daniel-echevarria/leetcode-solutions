const maxProfit = (prices) => {
  let bestPrice = prices[0];
  let maxProfit = 0;
  for (let i = 1; i < prices.length; i++) {
    if (prices[i] < bestPrice) bestPrice = prices[i];
    if (prices[i] > bestPrice) {
      let currentProfit = prices[i] - bestPrice;
      if (currentProfit > maxProfit) maxProfit = currentProfit;
    }
  }
  return maxProfit;
};

maxProfit([7, 1, 5, 3, 6, 4]);
maxProfit([7, 6, 4, 3, 1]);

// Given an array of prices
// declare the bestPrice the value of the first element
// declare maxProfit to 0
// iterate through the array from the second element
// if the current element is smaller than the bestPrice, update bestPrice with it
// if it's bigger check the difference between that price and the bestPrice
// if it's bigger than maxProfit update max Profit
// return maxProfit
