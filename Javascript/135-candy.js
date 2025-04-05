// given an array ratings that represents the ratings of the a line of children
// give at least one candy to every kid
// give more candies if the kid has a higher rating than the neighbor

// create an array candies with the same length as ratings and fill it with 1
// iterate through ratings  from index 1
// if the current rating is smaller than the previous one
// and the previous candy count is equal or smaller to the current candy count
// the previous candy count gets the current candy count + 1
// if the current rating is bigger than the previous one
// and the current candy count is smaller or equal to the previous candy count
// the current candy count gets the previous candy count + 1
// after the iteration return the sum of all candies

// Bruteforce solution
const bruteCandy = (ratings) => {
  const n = ratings.length;
  const candies = Array.from({ length: n }, () => 1);
  for (let i = 0; i < n; i++) {
    for (let i = 1; i < n; i++) {
      if (ratings[i] < ratings[i - 1] && candies[i - 1] <= candies[i])
        candies[i - 1] = candies[i] + 1;
      if (ratings[i] > ratings[i - 1] && candies[i] <= candies[i - 1])
        candies[i] = candies[i - 1] + 1;
    }
  }
  const sumOfCandies = candies.reduce((acc, current) => acc + current);
  console.log(sumOfCandies);
  return sumOfCandies;
};

// Algo for recursiveAllocation of candy
// Given a kid
// add 1 to that kid candy count
// if the kid is at index 0 return
// if the kid before has a smaller rating the current kid candy count gets the previous candy count + 1
// if the kid before has a bigger rating and the kid before it has less or the same amount of candy
// call recursive allocation on the previous kid

const candy = (ratings) => {
  const n = ratings.length;
  const candies = Array.from({ length: n }, () => 0);
  for (let i = 0; i < n; i++) recursiveAllocation(i, ratings, candies);
  const sumOfCandies = candies.reduce((acc, current) => acc + current);
  return sumOfCandies;
};

const recursiveAllocation = (i, ratings, candies) => {
  candies[i] += 1;
  if (i === 0) return;
  if (ratings[i - 1] < ratings[i] && candies[i - 1] >= candies[i])
    candies[i] = candies[i - 1] + 1;
  if (ratings[i - 1] > ratings[i] && candies[i - 1] <= candies[i]) {
    recursiveAllocation(i - 1, ratings, candies);
  }
};

// candy([1, 0, 2]);
// candy([1, 2, 2]);
// candy([1, 2, 87, 87, 87, 2, 1]);
candy([1, 6, 10, 8, 7, 3, 2]);
