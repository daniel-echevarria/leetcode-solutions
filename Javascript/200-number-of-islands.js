var numIslands = function (grid) {
  const graph = generateAgencyList(grid);
  const visited = new Set();
  const queue = [graph];
};

// Create a graph of agency with x,y coordinates
// where each coordinate gets a value and neighbors
const generateAgencyList = (grid) => {
  const height = grid.length;
  const width = grid[0].length;
  const adjacencyList = {};
  for (let i = 0; i < height; i++) {
    for (let j = 0; j < width; j++) {
      adjacencyList[`${i},${j}`] = {
        val: grid[i][j],
        neighbors: [
          [i - 1, j],
          [i + 1, j],
          [i, j - 1],
          [i, j + 1],
        ],
      };
    }
  }
  return adjacencyList;
};
