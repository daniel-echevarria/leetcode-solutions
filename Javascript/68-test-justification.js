var fullJustify = function (words, maxWidth) {
  const n = words.length;
  let result = [];
  let currentLine = [];
  let letterCount = 0;
  for (let i = 0; i < n; i++) {
    currentLine.push(words[i]);
    currentLine.push(" ");
    letterCount += words[i].length + 1;
    if (i + 1 > n - 1) {
      result.push(currentLine.join(""));
      currentLine = [];
      letterCount = 0;
      return result;
    }
    if (letterCount + words[i + 1].length > maxWidth) {
      result.push(currentLine.join(""));
      currentLine = [];
      letterCount = 0;
    }
  }
};

const res = fullJustify(
  ["This", "is", "an", "example", "of", "text", "justification."],
  16
);
console.log(res);

const res2 = fullJustify(
  ["What", "must", "be", "acknowledgment", "shall", "be"],
  16
);
console.log(res2);

const res3 = fullJustify(
  [
    "Science",
    "is",
    "what",
    "we",
    "understand",
    "well",
    "enough",
    "to",
    "explain",
    "to",
    "a",
    "computer.",
    "Art",
    "is",
    "everything",
    "else",
    "we",
    "do",
  ],
  20
);

console.log(res3);

// Algo fullJustify
// declare result with an initial value of []
// declare a currentLine with an initial value of []
// declare a letterCount with an initial value of 0
// Iterate through the words
// if letterCount + the next word length is bigger than maxWidth
// push the joined line to result
// currentLine gets []
// letterCount gets 0
// push the current word to currentLine
// add the current word length to letterCount
// push a white space

// push the word
// if the letterCount is bigger or equal to the maxWidth - 1
