// var canFinish = function (numCourses, prerequisites) {
//   const needsGraph = {};
//   for (const pre of prerequisites) {
//     const can = pre[0];
//     const must = pre[1];
//     if (needsGraph[can]) {
//       needsGraph[can].push(must);
//       continue;
//     }
//     needsGraph[can] = [must];
//   }
//   let loopExists = false;
//   let visited = new Set();
//   const BFS = (current, originalCourse) => {
//     if (visited.has(current) || !needsGraph[current] || loopExists) return;
//     visited.add(current);
//     const needs = needsGraph[current];
//     if (needs.includes(Number(originalCourse))) loopExists = true;
//     for (n of needs) {
//       BFS(n, originalCourse);
//       visited = new Set();
//     }
//   };
//   for (const key of Object.keys(needsGraph)) {
//     BFS(key, key);
//   }
//   return !loopExists;
// };

const canFinish = (numCourses, prerequisites) => {
  const mustTake = {};
  const mustBeTakenBy = {};
  for (const pre of prerequisites) {
    const a = pre[0];
    const b = pre[1];
    mustTake[a] ? mustTake[a].push(b) : (mustTake[a] = [b]);
    mustBeTakenBy[b] ? mustBeTakenBy[b].push(a) : (mustBeTakenBy[b] = [a]);
  }
  for (const [course, prerequisites] of Object.entries(mustBeTakenBy)) {
    for (const pre of prerequisites) {
      if (mustBeTakenBy[pre]) {
        for (const must of mustBeTakenBy[pre]) {
          mustTake[must].push(Number(course));
        }
      }
    }
  }
  console.log(mustTake, mustBeTakenBy);
  for (const course in mustTake) {
    if (mustTake[course].includes(Number(course))) return false;
  }
  return true;
};

const resultMustTake = {
  1: [0, 3, 0],
  2: [0],
  3: [1, 2],
};

// through prerequisites and make a map of the needsGraph
// Then iterate through the keys of the map and operate a Breadth first search
// that looks for the same value than the key
// Declare a set visited to keep track and avoid infinite loops
// if the bfs returns false return false
// after iteration return true

//  New Approach
//  Create a both a map of mustTake and mustBeTakenBy
//  When encountering  a new mustTake
