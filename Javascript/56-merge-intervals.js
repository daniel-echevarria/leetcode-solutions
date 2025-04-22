// Given an array of intervals where intervals[i] = [starti, endi],
// merge all overlapping intervals, and return an array of the non-overlapping
// intervals that cover all the intervals in the input.

const sortIntervals = (a, b) => a[0] - b[0];
const overlap = (a, b) => b[0] <= a[1];

var merge = function (intervals) {
  intervals.sort(sortIntervals);
  const result = [intervals[0]];
  for (let i = 1; i < intervals.length; i++) {
    const lastResult = result[result.length - 1];
    const current = intervals[i];
    if (overlap(lastResult, current)) {
      result.pop();
      result.push([lastResult[0], Math.max(lastResult[1], current[1])]);
      continue;
    }
    result.push(current);
  }
  return result;
};

// Algo
// Sort the intervals in non-decreasing order based on the first element of the interval
// declare a variable result that gets intervals[0]
// Iterate through the intervals from index 1
// Check if the last interval of result overlaps with the current interval
// if they do replace the last interval of result with
// an interval which gets on index 0
// the smallest of the first values of the intervals
// and on index 1 the biggest of the second values of the intervals
// otherwise just push the current interval
// after iteration return the result array

// Algo overlaps
// Given two intervals
// check if the first element of the second interval
// is equal of smaller than the second element
// if it is returns true otherwise return false

console.log(
  merge([
    [2, 6],
    [1, 3],
    [8, 10],
    [15, 18],
  ])
);
