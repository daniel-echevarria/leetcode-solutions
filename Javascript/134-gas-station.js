/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */

// Given an array of gas stations with the amount of gas available
// And an array of the cost from that station to the next
// Find if possible to make a full round
// iterate through gas
// for each index check if possible to do the full round
// if possible return the index
// otherwise go to next index
// if reach end of gas array, return -1

// const isPossibleToGoAround = (i, gas, cost) => {
//   let keepGoing = true;
//   let steps = 0;
//   let gasAvailable = 0;
//   let index = i;
//   while (keepGoing) {
//     gasAvailable += gas[index] - cost[index];
//     steps++;
//     index++;
//     if (index > gas.length - 1) index = 0;
//     if (gasAvailable < 0) return false;
//     if (steps === gas.length) return true;
//   }
// };

// var canCompleteCircuit = function (gas, cost) {
//   let answer = -1;
//   let i = 0;
//   while (i < gas.length) {
//     if (isPossibleToGoAround(i, gas, cost)) {
//       answer = i;
//       return;
//     }
//     i++;
//   }
//   return answer;
// };

// const gas = [1, 2, 3, 4, 5];
// const cost = [3, 4, 5, 1, 2];
// const gas = [2, 3, 4];
// const cost = [3, 4, 3];
// console.log(isPossibleToGoAround(2, gas, cost));
// console.log(isPossibleToGoAround(3, gas, cost));

// const result = canCompleteCircuit(gas, cost);
// console.log(result);

// Algo isPossibleToGoAround
// Given an index an array gas and an array cost
// declare a variable step with initial value 0
// declare a variable gasAvailable with an initial value of gas[index]
// declare a variable index with initial value of the passed index
// subtract cost[index] from gasAvailable
// if gasAvailable less than 0 return false
// otherwise step gets +1
// index gets + 1
// if the index is bigger than the gas length index gets 0
// if steps is equal to the gas array length return true

// newAlgo:
// from the two array make a total array by subtracting cost from gas for each index
// passed through the array twice keeping note of the steps and the total

const gas = [1, 2, 3, 4, 5];
const cost = [3, 4, 5, 1, 2];
// const gas = [2, 3, 4];
// const cost = [3, 4, 3];

const isPossibleToGoAround = (i, total) => {
  const n = total.length;
  let keepGoing = true;
  let steps = 0;
  let gasAvailable = 0;
  let index = i;
  while (keepGoing) {
    gasAvailable += total[i];
    steps++;
    index++;
    if (index > n - 1) index = 0;
    if (gasAvailable < 0) return false;
    if (steps === n) return true;
  }
};

const canCompleteCircuit = (gas, cost) => {
  const total = gas.map((val, i) => val - cost[i]);
  let answer = -1;
  let i = 0;
  while (i < total.length) {
    if (isPossibleToGoAround(i, total)) {
      answer = i;
      return answer;
    }
    i++;
  }
  return answer;
};

console.log(canCompleteCircuit(gas, cost));
