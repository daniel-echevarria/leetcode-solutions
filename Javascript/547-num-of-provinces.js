var findCircleNum = function (isConnected) {
  const n = isConnected.length;
  let numProvinces = 0;
  const dfs = (i, j) => {
    if (i < 0 || j < 0 || i > n - 1 || j > n - 1 || isConnected[i][j] == 0)
      return;
    isConnected[i][j] = 0;
    dfs(i + 1, j);
    dfs(i - 1, j);
    dfs(i, j + 1);
    dfs(i, j - 1);
  };
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (isConnected[i][j] == 0) continue;
      numProvinces++;
      dfs(i, j);
    }
  }
  return numProvinces;
};

findCircleNum([
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1],
]);

// Declare a variable numOfProvinces with initial value of 0
// Iterate through all the cities in isConnected
// if the value of the city is 0 continue
// if the value of the city is 1,
// add one to numProvinces
// call dfs on the city
// the dfs goes as such:
// if the value is 0 return
// if the value is 1, it becomes 0
// if it's out of bounds return
// call dfs on all the neighbors
