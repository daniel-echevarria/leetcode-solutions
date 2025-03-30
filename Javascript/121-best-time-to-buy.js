var maxProfit = function (prices) {
  let buyDay = 0;
  let sellDay = -1;
  let i = 1;
  let j = -2;
  let maxProfit = 0;
  let keepGoing = true;
  while (keepGoing) {
    if (prices.length + j > i) {
      if (prices.at(j) > prices.at(sellDay)) sellDay = j;
    }
    if (i > prices.length + sellDay) break;
    if (prices[i] < prices[buyDay]) buyDay = i;
    i++;
    j--;
    if (buyDay > prices.length + j) keepGoing = false;
    if (prices.length + sellDay < i) keepGoing = false;
  }
  const currentProfit = prices.at(sellDay) - prices[buyDay];
  if (currentProfit > maxProfit) maxProfit = currentProfit;
  return maxProfit;
};

// maxProfit([7, 1, 5, 3, 6, 4]);
// maxProfit([1, 4, 2]);
// maxProfit([3, 2, 6, 5, 0, 3]);
maxProfit([7, 4, 1, 2]);
// maxProfit([2, 1, 2, 1, 0, 0, 1]);

// Given a list of prices
// declare buyDayIndex with a value of 0
// declare sellDayIndex with a value of -1
// declare a variable i with value 1
// declare a variable j with value -2
// loop until i is bigger or equal to sellDayIndex
// at each round compare the value at i with the value at buyDayIndex if it's smaller update buyDayIndex with i
// compare j with the value of sellIndex if it's bigger update sellIndex
// return the value at sellIndex minus the value at buyDayIndex
