const sortIntervals = (a, b) => a[0] - b[0];

const overlap = (a, b) => a[1] >= b[0];
const merge = (a, b) => [a[0], Math.max(a[1], b[1])];

var findMinArrowShots = function (points) {
  points.sort(sortIntervals);
  const result = [points[0]];
  for (let i = 1; i < points.length; i++) {
    const last = result[result.length - 1];
    const curr = points[i];
    console.log(last, currf);
    if (overlap(last, curr)) {
      result.pop();
      result.push(merge(last, curr));
      continue;
    }
    result.push(curr);
  }
  console.log(result);
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
