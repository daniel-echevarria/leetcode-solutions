var maxArea = function (height) {
  const n = height.length;
  let i = 0;
  let j = n - 1;
  let maxWater = 0;
  while (j > i) {
    let waterArea = getWaterArea(i, j, height);
    if (waterArea > maxWater) maxWater = waterArea;
    height[i] >= height[j] ? j-- : i++;
  }
  return maxWater;
};

const getWaterArea = (i, j, height) => {
  const horizontal = j - i;
  const vertical = height[i] < height[j] ? height[i] : height[j];
  return horizontal * vertical;
};

// Given an array of numbers height
// declare a variable i with initial value of 0
// declare a variable j with initial value of height length - 1
// declare a variable maxWater with initial value of 0
// Loop until j is smaller than i
// calculate waterArea
// if waterArea is bigger than maxWater, update maxWater
// i gets + 1
// calculate waterArea
// if waterArea is bigger than maxWater, update maxWater
// j gets -1

// Algo waterArea
// declare a variable horizontal that gets i minus j
// declare a variable vertical that gets the smallest of
// the two values height[i] and height[j]
// return the multiplication of these values
console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]));
console.log(maxArea([1, 1]));
console.log(maxArea([8, 7, 2, 1]));
