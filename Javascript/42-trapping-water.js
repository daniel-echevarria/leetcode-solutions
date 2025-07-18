var trap = function (height) {
  let left = 0;
  let right = 1;
  let trappedWater = 0;
  let lastRightWall = 0;
  for (let i = height.length - 1; i >= 0; i--) {
    if (height[i] > height[i - 1]) {
      lastRightWall = i;
      break;
    }
  }
  if (lastRightWall == 0) return 0;
  height = height.slice(0, lastRightWall + 1);
  while (right < height.length) {
    if (height[left] <= height[right]) {
      left++;
      right++;
    } else {
      let potentialWater = 0;
      while (height[right] < height[left] && right < height.length) {
        potentialWater += height[left] - height[right];
        right++;
      }
      if (right == height.length) {
        height[left] = Math.max(...height.slice(left + 1, height.length));
        right = left + 1;
        potentialWater = 0;
      } else {
        trappedWater += potentialWater;
        left = right;
        right = left + 1;
      }
    }
  }
  return trappedWater;
};

// First 'clean' the array by removing all values on the left and on the right
// as long as they are smaller than the next
// Declare a variable left with initial value of 0
// Declare a variable right with initial value of 1
// Declare a variable tappedWater with initial value of 0
// Loop until right equals height.length - 1
// If the value at left is smaller or equals as the value at right both gets ++
// If the value of left is bigger than the value at right check how much water is trapped
// For that loop until right value is bigger or equal to the left value while at each
// element adding the trapped water following the rule left - current value
// Return the trappedWater
