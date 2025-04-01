var maxProfit = function (prices) {
  let profit = 0;
  for (let i = 1; i < prices.length; i++) {
    if (prices[i] > prices[i - 1]) {
      profit += prices[i] - prices[i - 1];
    }
  }
  console.log(profit);
  return profit;
};

maxProfit([7, 1, 5, 3, 6, 4]);
maxProfit([1, 2, 3, 4, 5]);

// Given an array of prices
// declare a variable profit
// iterate through the array from second element
// if the current element is smaller than the previous do nothing
// if it's bigger at the difference to profit
