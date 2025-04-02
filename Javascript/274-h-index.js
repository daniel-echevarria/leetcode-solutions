function compareNumbers(a, b) {
  return a - b;
}

var hIndex = function (citations) {
  const sorted = citations.sort(compareNumbers).reverse();
  let bestH = 0;
  for (let i = 0; i < sorted.length; i++) {
    if (sorted[i] >= i + 1) bestH = i + 1;
    if (i + 1 > sorted[i]) return bestH;
  }
  return bestH;
};

hIndex([3, 0, 6, 1, 5]);
console.log(hIndex([3, 0, 6, 1, 5]));
console.log(hIndex([1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3]));

// Given an array of numbers
// sort the array and reverse it
// iterate through the array
// if the value is bigger than the index + 1
// bestH gets the index + 1
