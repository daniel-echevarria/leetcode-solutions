// var insert = function (intervals, newInterval) {
//   const previousIndex = intervals.findIndex((x) => x[0] <= newInterval[0]);
//   if (previousIndex === -1) return [newInterval, ...intervals];
//   if (overlap(intervals[previousIndex], newInterval)) {
//     intervals[previousIndex] = merge(intervals[previousIndex], newInterval);
//   } else {
//     intervals.splice(previousIndex, newInterval);
//   }
//   const result = [intervals[0]];
//   for (let i = 1; i < intervals.length; i++) {
//     const pre = result[i - 1];
//     const current = intervals[i];
//     if (overlap(pre, current)) {
//       result.push(merge(pre, current));
//       continue;
//     }
//     result.push(current);
//   }
//   return result;
// };

const sortIntervals = (a, b) => a[0] - b[0];
const merge = (a, b) => [a[0], Math.max(a[1], b[1])];
const overlap = (a, b) => a[1] >= b[0];

var insert = function (intervals, newInterval) {
  intervals.push(newInterval);
  intervals.sort(sortIntervals);
  const result = [intervals[0]];
  for (let i = 1; i < intervals.length; i++) {
    const last = result[result.length - 1];
    const current = intervals[i];
    if (overlap(last, current)) {
      result.pop();
      result.push(merge(last, current));
      continue;
    }
    result.push(current);
  }
  return result;
};

// console.log(
//   insert(
//     [
//       [1, 3],
//       [6, 9],
//     ],
//     [2, 5]
//   )
// );

console.log(
  insert(
    [
      [1, 2],
      [3, 5],
      [6, 7],
      [8, 10],
      [12, 16],
    ],
    [4, 8]
  )
);

// Algo insert interval
// find the first interval in which the interval start is  smaller or equals than the newInterval start
// if none is find, return an array like [newInterval, ...intervals]
// otherwise merge the intervals
// iterate through the remaining intervals and if they overlap merge them
