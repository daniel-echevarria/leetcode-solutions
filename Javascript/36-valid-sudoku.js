var isValidSudoku = function (board) {
  const sudoku = [...getSquares(board), ...getColumns(board), ...board];
  for (let i = 0; i < sudoku.length; i++) {
    if (containsDuplicates(sudoku[i])) return false;
  }
  return true;
};

// Algo
// make an array of the squares
// make an array of the columns
// iterate through all columns, squares and lines
// if found a duplicate other than . return false
// after iteration return true

// getSquare algo
// board

// algo containsDuplicates
// filter all dots
// check if the length of the result is the same length as a set of the values

const containsDuplicates = (array) => {
  const clean = array.filter((x) => x != ".");
  const mySet = new Set(clean);
  return !(clean.length === mySet.size);
};

const getSquares = (board) => {
  const squares = [
    ...getFirst3(board),
    ...getSecond3(board),
    ...getLast3(board),
  ];
  return squares;
};

const getColumns = (board) => {
  const columns = board[0].map((_, colIndex) =>
    board.map((row) => row[colIndex])
  );
  return columns;
};

const getFirst3 = (board) => {
  let row = 0;
  let col = 0;
  const first3 = Array.from({ length: 3 }, () => []);
  while (row < 3) {
    if (col < 3) {
      first3[0].push(board[row][col]);
    } else if (col < 6) {
      first3[1].push(board[row][col]);
    } else {
      first3[2].push(board[row][col]);
    }
    col++;
    if (col > 8) {
      row++;
      col = 0;
    }
  }
  return first3;
};

const getSecond3 = (board) => {
  let row = 3;
  let col = 0;
  const second3 = Array.from({ length: 3 }, () => []);
  while (row < 6) {
    if (col < 3) {
      second3[0].push(board[row][col]);
    } else if (col < 6) {
      second3[1].push(board[row][col]);
    } else {
      second3[2].push(board[row][col]);
    }
    col++;
    if (col > 8) {
      row++;
      col = 0;
    }
  }
  return second3;
};

const getLast3 = (board) => {
  let row = 6;
  let col = 0;
  const last3 = Array.from({ length: 3 }, () => []);
  while (row < 9) {
    if (col < 3) {
      last3[0].push(board[row][col]);
    } else if (col < 6) {
      last3[1].push(board[row][col]);
    } else {
      last3[2].push(board[row][col]);
    }
    col++;
    if (col > 8) {
      row++;
      col = 0;
    }
  }
  return last3;
};

// console.log(
//   isValidSudoku([
//     ["8", "3", ".", ".", "7", ".", ".", ".", "."],
//     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
//     [".", "9", "8", ".", ".", ".", ".", "6", "."],
//     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
//     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
//     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
//     [".", "6", ".", ".", ".", ".", "2", "8", "."],
//     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
//     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
//   ])
// );

console.log(
  isValidSudoku([
    ["7", ".", ".", ".", "4", ".", ".", ".", "."],
    [".", ".", ".", "8", "6", "5", ".", ".", "."],
    [".", "1", ".", "2", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "9", ".", ".", "."],
    [".", ".", ".", ".", "5", ".", "5", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
  ])
);

// declare a variable first3 with an array of 3 empty arrays
// Declare a variable row with initial of 0
// declare a variable col with initial value of 0
// if col is smaller than 3 push it to the first empty array
// if col is smaller than 6 push it to the second array
// otherwise push it to the 3rd array
// each turn col gets +1
// if col is 9
// row gets + 1 and col gets 0
