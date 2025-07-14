var findCircleNum = function (isConnected) {};

// Declare a variable n that gets isConnected length
// Iterate through isConnected and make a graph of the connected cities as such:
// if i,j == 1
// if i == j add j to i or create i:j
// then check if i exits and add j or create i: j
// do the same for j, check if j exits, add i if yes or create
// if i,j == 0 continue
// this gives is a graph of the adjacency list

// Declare a visited set
// Then we iterate from 0 to n - 1
// if the city  is in the visited set or not in the graph we continue
// If we find the city in the graph we
// add 1 to the provinces and launch dfs
// the dfs goes until all the neighbors are visited
// it returns if the node is visited
// otherwise it adds the node anc calls dfs in all the neighbors

// finally return numProvinces
