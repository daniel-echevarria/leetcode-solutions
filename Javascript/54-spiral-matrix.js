var spiralOrder = function (matrix) {
  let m = matrix.length;
  let n = matrix[0].length;
  let row = 0;
  let col = 0;
  let indexes = [];
  let rowDirection = 1;
  let colDirection = 1;
  while (indexes.length < m * n) {
    while (col < n) {
      indexes.push([row, col]);
      col++;
    }
    col--;
    row++;
    while (row < m) {
      indexes.push([row, col]);
      row++;
    }
    row--;
    col--;
    while (col > -1) {
      indexes.push([row, col]);
      col--;
    }
    col++;
    row--;
    while (row > 0) {
      indexes.push([row, col]);
      row--;
    }
  }

  return indexes;
};

// Algo
// declare a variable m that gets matrix length
// declare a variable n that gets matrix[0].length
// declare a variable row that gets 0
// declare a variable col that gets 0
// declare an empty array indexes []
// declare a rowDirection with initial value of 1
// declare a colDirection with initial value of 1
// Launch a loop that stops when the length of indexes is the same m * n
// while the col number is smaller than the n
// push [row, col]
// after add one to row
// while the row number is smaller than m
// push [row, col]
// after remove one from col
// while the col number is bigger than -1
// push [row, col]
// after remove one from row
// while the row is

console.log(
  spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ])
);
