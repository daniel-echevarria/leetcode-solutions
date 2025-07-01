// var findJudge = function (n, trust) {
//   const labels = Array.from({ length: n }, (_, i) => i + 1);
//   const trustGraph = {};
//   for (const pair of trust) {
//     const a = pair[0];
//     const b = pair[1];
//     trustGraph[a] ? trustGraph[a].push(b) : (trustGraph[a] = [b]);
//   }
//   console.log(trustGraph);
//   const trusting = Object.keys(trustGraph).map((key) => +key);
//   const judges = labels.filter((label) => !trusting.includes(label));
//   if (judges.length != 1) return -1;
//   const judge = judges[0];
//   for (people in trustGraph) {
//     if (trustGraph[people].includes(judge)) continue;
//     return -1;
//   }
//   return judge;
// };

// Make an array of labels from 1 to n
// Iterate through trust and make a graph of the trust
// Get all the keys from the graph
// Find the only value in n that is not a key of the graph
// If there is no such value return -1
// If there is, confirm that that value is present in an all arrays of the trust graph

// const findJudge = (n, trust) => {
//   let judge = -1;
//   const graph = {};
//   for (let i = 1; i <= n; i++) {
//     const trusting = trust
//       .filter((pair) => pair[0] == i)
//       .map((pair) => pair[1]);
//     if (trusting.length == 0) {
//       if (judge == -1) {
//         judge = i;
//         continue;
//       } else {
//         return -1;
//       }
//     }
//     graph[i] = trusting;
//   }
//   for (const people in graph) {
//     if (graph[people].includes(judge)) continue;
//     return -1;
//   }
//   return judge;
// };

// New Algo
// Declare a variable judge with initial value of -1
// Iterate from 1 to n
// At each iteration find all the pairs in trust that match trust[0] == i
// Add the pair to the graph
// If one label has no pair, judge gets i or return -1 if judge was already selected
// After iteration check if all the people in the graph trust the judge
// if yest return the judge otherwise return -1

var findJudge = function (n, trust) {
  if (n == 1) return 1;
  const howManyTrusts = {};
  const trusting = new Set();
  let judge = null;
  let maxTrust = 0;
  for (const pair of trust) {
    a = pair[0];
    b = pair[1];
    trusting.add(a);
    const totalTrusts = (howManyTrusts[b] || 0) + 1;
    howManyTrusts[b] = totalTrusts;
    if (totalTrusts > maxTrust) judge = b;
    maxTrust = Math.max(maxTrust, totalTrusts);
  }
  if (howManyTrusts[judge] == n - 1 && !trusting.has(judge)) return judge;
  return -1;
};
