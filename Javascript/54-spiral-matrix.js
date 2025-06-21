var spiralOrder = function (matrix) {
  let top = 0;
  let bottom = matrix.length - 1;
  let left = 0;
  let right = matrix[0].length - 1;

  const elements = [];
  while (top <= bottom && left <= right) {
    for (let i = left; i <= right; i++) {
      elements.push(matrix[top][i]);
    }
    top++;

    for (let i = top; i <= bottom; i++) {
      elements.push(matrix[i][right]);
    }
    right--;

    if (top <= bottom) {
      for (let i = right; i >= left; i--) {
        elements.push(matrix[bottom][i]);
      }
      bottom--;
    }

    if (left <= right) {
      for (let i = bottom; i >= top; i--) {
        elements.push(matrix[i][left]);
      }
      left++;
    }
  }
  return elements;
};

// Declare four 'layers' top, right, bottom, left with the values based on the
// m and n
// Loop while left is smaller than right and top is bigger than bottom
// inside the loop iterate through from left to right
// then from top to bottom
// then from right to left
// then from bottom to top
// pushing the elements to an array
// after each iteration remove one from the layer or add one depending on the case
