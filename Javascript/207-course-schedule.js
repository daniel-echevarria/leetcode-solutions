var canFinish = function (numCourses, prerequisites) {
  const needsGraph = {};
  for (const pre of prerequisites) {
    const can = pre[0];
    const must = pre[1];
    if (needsGraph[can]) {
      needsGraph[can].push(must);
      continue;
    }
    needsGraph[can] = [must];
  }
  let loopExists = false;
  const visited = new Set();
  const BFS = (current, originalCourse) => {
    if (visited.has(current) || !needsGraph[current]) return;
    visited.add(current);
    const needs = needsGraph[current];
    if (needs.includes(Number(originalCourse))) loopExists = true;
    for (n of needs) {
      BFS(n, originalCourse);
    }
  };
  for (const key in Object.keys(needsGraph)) {
    BFS(key, key);
  }
  return !loopExists;
};

// Iterate through prerequisites and make a map of the needsGraph
// Then iterate through the keys of the map and operate a Breadth first search
// that looks for the same value than the key
// Declare a set visited to keep track and avoid infinite loops
// if the bfs returns false return false
// after iteration return true
