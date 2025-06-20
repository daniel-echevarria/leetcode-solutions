var spiralOrder = function (matrix) {
  const elements = [];
  const matrixNavigation = {
    row: 0,
    col: 0,
    getCurrentPosition: () =>
      matrix[matrixNavigation.col][matrixNavigation.row],
    moveRight: () => matrixNavigation.row++,
    moveLeft: () => matrixNavigation.row--,
    moveDown: () => matrixNavigation.col++,
    moveUp: () => matrixNavigation.col--,
  };
  const matrixSize = matrix.length * matrix[0].length;
  count = 0;
  while (matrixNavigation.getCurrentPosition()) {
    elements.push(matrixNavigation.getCurrentPosition());
    matrixNavigation.moveRight();
  }
  matrixNavigation.moveLeft();
  while (matrixNavigation.getCurrentPosition()) {
    console.log(matrixNavigation.getCurrentPosition());
    elements.push(matrixNavigation.getCurrentPosition());
    matrixNavigation.moveDown();
  }
  console.log(elements);
};

spiralOrder([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]);

// Declare an array elements
// Declare an initial coordinates of { 0, 0 }
// Iterate through the matrix following this pattern go as right as possible while collecting the elements
// go as down as possible while connecting the elements
// go as left as possible while collecting the elements
// go as up as possible while collecting the elements
// keep going until no more elements
