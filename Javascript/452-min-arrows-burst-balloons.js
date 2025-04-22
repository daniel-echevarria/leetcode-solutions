const sortIntervals = (a, b) => a[0] - b[0];

const overlap = (a, b) => a[1] >= b[0];
const merge = (a, b) => [a[0], Math.max(a[1], b[1])];

var findMinArrowShots = function (points) {
  points.sort(sortIntervals);
  const result = [points[0]];
  for (let i = 1; i < points.length; i++) {
    const last = result[result.length - 1];
    const curr = points[i];
    if (overlap(last, curr)) {
      result.pop();
      result.push([last[0], Math.min(last[1], curr[1])]);
      continue;
    }
    result.push(curr);
  }
  return result.length;
};

console.log(
  findMinArrowShots([
    [10, 16],
    [2, 8],
    [1, 6],
    [7, 12],
  ])
);

console.log(
  findMinArrowShots([
    [3, 9],
    [7, 12],
    [3, 8],
    [6, 8],
    [9, 10],
    [2, 9],
    [0, 9],
    [3, 9],
    [0, 6],
    [2, 8],
  ])
);

// Algo
// Sort the points based on the start
// declare a variable result with an initial value of an array with the first point
// Iterate through the points
// if the point overlaps with the last value of result do nothing
// otherwise push the current value
