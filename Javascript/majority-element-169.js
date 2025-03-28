var majorityElement = function (nums) {
  let maxVotes = 0;
  let winner = null;
  let votesCount = {};
  nums.forEach((element) => {
    votesCount[element] ? votesCount[element]++ : (votesCount[element] = 1);
  });
  Object.keys(votesCount).forEach((key) => {
    if (votesCount[key] > maxVotes) {
      maxVotes = votesCount[key];
      winner = key;
    }
  });
  return +winner;
};

majorityElement([2, 2, 1, 1, 1, 2, 2]);
majorityElement([3, 2, 3]);

// given an array with many elements divided between 2 different values
// declare a variable maxVotes with a value of 0
// declare a variable winner with a value of null
// create an object votesCount
// iterate through the array
// if the key already exists in the object add 1 to it
// create an array from the keys
// iterate through the keys,
// if the value of that key is bigger than max votes,
// update max votes with that value and update winner with the key
// return winner
